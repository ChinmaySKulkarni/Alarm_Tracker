# DESCRIPTION:
# -Parse Alarms using Pyspark which is the Python implementation for
#  Apache Spark APIs.
#
# -The 'SPARK_HOME' environment variable defines the location of the 
#  Apache Spark installation. The pyspark utility can be found at:
#  $SPARK_HOME/bin/pyspark
#
#
# EXECUTION:
# -To run this program, give the following command to submit the 
#  Apache Spark job:
#  $SPARK_HOME/bin/spark-submit  <python file>
#	
#
# RESOURCES:
# -pyspark API Documentation: https://spark.apache.org/docs/latest/api/python/
#
# -Explanation of functions/APIs used:
#
#	SparkContext():
#	The main entry point for Spark functionality and it 
#	represents the connection to a Spark cluster, 
#	and can be used to create an RDD and broadcast variables on that cluster.
#
#	textFile():
#	This  method will read a text file from HDFS, a local file system 
#	(available on all nodes), or any Hadoop-supported file system URI, 
#	and return it as an RDD of Strings.
#
#	cache():
#	This method is used to persist this RDD with the default storage level 
#	(MEMORY_ONLY_SER).
#
#	filter():
#	This method returns a new RDD containing only the elements that satisfy a 
#	predicate.
#
#	count():
#	Returns the number of elements in that RDD.
#
#
# CREATED BY: 
# Chinmay Kulkarni

from pyspark import SparkContext

#Get the RDD strings from the supplied file.
def getRDDStrings(logFile):
	sc = SparkContext("local", "Spark Parser")
	RDDLog = sc.textFile(logFile).cache()
	return RDDLog


#Counts the number of lines containing 'A's and 'B's.
def textProcessing(RDDStrings):
	numAs = RDDStrings.filter(lambda s: 'a' in s).count()
	numBs = RDDStrings.filter(lambda s: 'b' in s).count()
	return numAs,numBs


if __name__ == "__main__":
	logFile = "./test.txt"
	RDDStrings = getRDDStrings(logFile)
	numAs, numBs = textProcessing(RDDStrings)
	print "No of lines with A:\t",numAs
	print "No of lines with B:\t",numBs

