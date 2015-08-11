# Parse Alarms using Pyspark which is the Python implementation for
# Apache Spark.
#
# SPARK_HOME defines the location of the Apache Spark installation.
# The pyspark utility can be found at:
#
# $SPARK_HOME/bin/pyspark
#	
# pyspark API Documentation: https://spark.apache.org/docs/latest/api/python/
#
# Created By: Chinmay Kulkarni
from pyspark import SparkContext

logfile = "./test.txt"
#A SparkContext represents the connection to a Spark cluster, 
#and can be used to create an RDD and broadcast variables on that cluster.
sc = SparkContext("local", "Sample Parser")

