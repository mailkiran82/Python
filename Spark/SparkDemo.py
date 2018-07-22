#!python3 SparkDemo.py
import findspark
findspark.init('/home/ubuntu/spark-2.1.1-bin-hadoop2.7')
import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct,avg,stddev

spark = SparkSession.builder.appName('ops').getOrCreate()
df = spark.read.csv('test.csv',inferSchema=True, header=True)

#df.printSchema()
#df.show()

#df.filter("id == 4").show()
#df.filter("id == 4").select('name').show()
#df.filter("id == 4").select(['id','name']).show()

#df.filter(df['id'] == 4).show()
#df.filter(df['id'] == 4).select(['name','id']).show()

#df.filter( (df['id'] ==  3) & (df['name'] == 'c')).select(['name','id']).show()

#result = df.filter( (df['id'] ==  3) & (df['name'] == 'c')).collect()
#print(result[0])

#row = result[0]
#d = row.asDict()
#print(d)

#print(row.asDict()['name'])

df.groupBy('name').count().show()
df.agg({'name':'count'}).show()

df.select(countDistinct('name').alias('mycount')).show()

print("Done")
