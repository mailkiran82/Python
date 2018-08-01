#!python3 SparkTest.py
import findspark
findspark.init('/home/ubuntu/spark-2.1.1-bin-hadoop2.7')
import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct,avg,stddev

import boto3

s3 = boto3.resource('s3')
s3.Object('mailkiran82','SparkData/TestData.csv').download_file('./TD.csv')
spark = SparkSession.builder.appName('ops').getOrCreate()
df = spark.read.csv('TD.csv',inferSchema=True, header=True)


def getCount():
    result =  df.select(countDistinct('name').alias('mycount')).collect()
    row = result[0]
    d = row.asDict()
    v = d['mycount']
    return v

def main():
    res = getCount()
    print(res)
    print("Done")

if __name__ == '__main__':
    main()
