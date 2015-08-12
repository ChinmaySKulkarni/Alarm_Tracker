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
# -To deploy on a cluster instead of a local machine, make changes to
#  SparkConf() parameters.
#
#
# RESOURCES:
# -pyspark API Documentation: https://spark.apache.org/docs/latest/api/python/
#  This URL will be referred to as "API_DOCs".
#
# -Explanation of functions/APIs used:
#
#	SparkConf():
#	Configuration for a Spark application. Used to set various Spark 
#	parameters as key-value pairs. For more info, see:
#	"API_DOCS"/pyspark.html?highlight=sparkconf#pyspark.SparkConf
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
#	collect():
#	Returns the contents of the RDD as a list.
#
# CREATED BY: 
# Chinmay Kulkarni

from pyspark import SparkConf, SparkContext

#Global Variables:
logFile = "./XML_Parsing/sample_alarms.xml"
IDFile = "./XML_Parsing/sample_IDs.txt"


#Set up Apache Spark configurations.
def configureSpark():
	conf = SparkConf()
	conf.setMaster("local")
	conf.setAppName("Apache Spark Alarm Parser")
	conf.set("spark.executor.memory", "1g")
	sc = SparkContext(conf = conf)
	return sc


#Get the RDD strings from the supplied file.
def getRDDStrings(sc,logFile):
	RDDLog = sc.textFile(logFile).cache()
	return RDDLog


#Counts the number of lines containing 'A's and 'B's.
def exampleTextProcessing(RDDStrings):
	numAs = RDDStrings.filter(lambda s: 'a' in s).count()
	numBs = RDDStrings.filter(lambda s: 'b' in s).count()
	return numAs,numBs


#Gets the matching ID from device or managed-object fields of an alarm message
def getDeviceManagedObjectsID(RDDStrings,IDRDDStrings):
	devices = RDDStrings.filter(lambda x : "<device>" in x)
	mgdObjects = RDDStrings.filter(lambda x : "<managed-object>" in x)
	devices = devices.collect().pop().strip()
	devices = devices.lstrip("<device>").rstrip("</device>")

	mgdObjects = mgdObjects.collect().pop().strip()
	mgdObjects = mgdObjects.lstrip("<managed-object>")
	mgdObjects = mgdObjects.rstrip("</managed-object>")
	for ID in IDRDDStrings.collect():
		ID = ID.strip()
		if ID in devices:
			return ID
		elif ID in mgdObjects:
			return ID
		else:
			return False


if __name__ == "__main__":
	sc = configureSpark()
	RDDStrings = getRDDStrings(sc,logFile)
	IDRDDStrings = getRDDStrings(sc,IDFile)
	ID = getDeviceManagedObjectsID(RDDStrings,IDRDDStrings)	
	print "\n\n\n"
	if not ID:
		print "No match."
	else:
		print "ID got is:\t", ID
	print "\n\n\n"
