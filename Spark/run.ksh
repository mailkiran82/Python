#!/bin/bash
if [ "$1" = "test" ];
then
python3 /opt/TestSparkTest.py
else
python3 /opt/SparkTest.py
fi
