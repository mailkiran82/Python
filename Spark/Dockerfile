FROM ubuntu
RUN apt-get update
RUN apt install -y python3-pip
RUN apt-get install -y default-jre
RUN apt-get install -y scala

ADD http://archive.apache.org/dist/spark/spark-2.1.1/spark-2.1.1-bin-hadoop2.7.tgz /tmp/
RUN tar -C /usr/local/bin/ -zxvf /tmp/spark-2.1.1-bin-hadoop2.7.tgz \
    && rm /tmp/spark-2.1.1-bin-hadoop2.7.tgz

RUN pip3 install py4j
RUN pip3 install findspark
RUN pip3 install boto3
RUN pip3 install pandas
RUN pip3 install smart_open

COPY SparkTest.py /opt/SparkTest.py

ENTRYPOINT python3 /opt/SparkTest.py