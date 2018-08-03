#!python3 SparkTest.py
import findspark
findspark.init('/usr/local/bin/spark-2.1.1-bin-hadoop2.7')
import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct,avg,stddev
from pyspark.sql.types import StructType,StructField,IntegerType,StringType

#import boto3
import timeit
import pandas as pd
import io
import smart_open as so

# get the file into pandas dataframe as object
header=True
headerList=None
pdf=pd.DataFrame()
with so.smart_open('s3://mailkiran82/SparkData/TestData.csv') as fin:
    for line in fin:
        if(header):
            headerList=list(line.decode('utf-8').lstrip().rstrip().split(','))
            header=False
        else:
            rec=pd.DataFrame([list(line.decode('utf-8').lstrip().rstrip().split(','))],columns=headerList)
            pdf=pd.concat([pdf,rec],ignore_index=True)

print("smart_open time:")
print(timeit.timeit('''
import pandas as pd
import smart_open as so
header=True
headerList=None
pdf=pd.DataFrame()
with so.smart_open('s3://mailkiran82/SparkData/TestData.csv') as fin:
    for line in fin:
        if(header):
            headerList=list(line.decode('utf-8').lstrip().rstrip().split(','))
            header=False
        else:
            rec=pd.DataFrame([list(line.decode('utf-8').lstrip().rstrip().split(','))],columns=headerList)
            pdf=pd.concat([pdf,rec],ignore_index=True)
''',number=1))

#pdf['id']=pdf['id'].astype(int)
#print(pdf.head())
#print(pdf.info())

print("boto3 => dataframe:")
print(timeit.timeit('''
import boto3
import pandas as pd
import io
s3 = boto3.client('s3')
res = s3.get_object(Bucket='mailkiran82',Key='SparkData/TestData.csv')
text = res['Body'].read().decode('utf-8')
pdf1 = pd.read_csv(io.StringIO(text))
''',number=1))
#print(pdf1.head())
#print(pdf1.info())

print("boto3 => file => dataframe:")
print(timeit.timeit('''
import boto3
import pandas as pd
s3 = boto3.resource('s3')
s3.Object('mailkiran82','SparkData/TestData.csv').download_file('./TD.csv')
pdf2 = pd.read_csv('TD.csv')
''',number=1))
#print(pdf2.head())
#print(pdf2.info())

#populate Spark dataframe from pandas dataframe
spark = SparkSession.builder.appName('ops').getOrCreate()
#schema = StructType([StructField('id',StringType(),True)\
#                     ,StructField('name',StringType(),True)])
#df = spark.createDataFrame(pdf,schema=schema)
df = spark.createDataFrame(pdf)


def getCount():
    result =  df.select(countDistinct('name').alias('mycount')).collect()
    row = result[0]
    d = row.asDict()
    v = d['mycount']
    return v

def main():
    res = getCount()
    print(res)
    print('Done')

if __name__ == '__main__':
    main()

