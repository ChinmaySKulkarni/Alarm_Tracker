# DESCRIPTION:
# -Parse Alarms to find the service ID that each alarm corresponds to 
#  using Pyspark which is the Python implementation for
#  Apache Spark APIs. This program will return a hashmap with keys as the alarm
#  number and value as the matching ID. Correspondingly, action can be taken
#  on those serviceIDs.
#
# -The 'SPARK_HOME' environment variable defines the location of the 
#  Apache Spark installation. The pyspark utility can be found at:
#  $SPARK_HOME/bin/pyspark
#
#
# EXECUTION:
# -To run this program, give the following command to submit the 
#  Apache Spark job:
#  $SPARK_HOME/bin/spark-submit  <this file>
#
# -Set the Alarms file location in the "logFile" variable as an HDFS URI or 
#  local file. The ID list against which to be matched can be provided in the
#  "IDFile" variable. 
#	
# -To deploy on a cluster instead of a local machine, make changes to
#  SparkConf() parameters.
#
#
# RESOURCES:
# -pyspark API Documentation: https://spark.apache.org/docs/latest/api/python/
#  This URL will be referred to as "API_DOCs".
#
# -Explanation of pySpark APIs used:
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
def exampleTextProcessing(alarmsRDD):
	numAs = alarmsRDD.filter(lambda s: 'a' in s).count()
	numBs = alarmsRDD.filter(lambda s: 'b' in s).count()
	return numAs,numBs


#Remove XML tags.
def preprocessRDD(RDD,field):
	openBracket = "<" + field + ">"
	closeBracket = "</" + field + ">"
	RDD = RDD.collect()
	for value in RDD:
		value = value.strip()
		value = value.lstrip(openBracket).rstrip(closeBracket)
	return RDD


#Gets the matching ID from device or managed-object fields of an alarm message
def getDeviceManagedObjectsID(sc,alarmsRDD,IDsRDD):
	devices = alarmsRDD.filter(lambda x : "<device>" in x)
	mgdObjects = alarmsRDD.filter(lambda x : "<managed-object>" in x)
	devices = preprocessRDD(devices,"device")
	mgdObjects = preprocessRDD(mgdObjects,"managed-object")
	
	alarmIDMappings = {}
	totalDevices = len(devices)
	totalMgdObjs = len(mgdObjects)
	if totalDevices < totalMgdObjs:
		totalAlarms = totalDevices
	else:
		totalAlarms = totalMgdObjs
	for i in xrange(0,totalAlarms):
		alarmIDMappings[i] = False
		for ID in IDsRDD.collect():
			ID = ID.strip()
			if ID in devices[i]:
				alarmIDMappings[i] = ID
				break
			elif ID in mgdObjects[i]:
				alarmIDMappings[i] = ID
				break
	return alarmIDMappings


if __name__ == "__main__":
	sc = configureSpark()
	alarmsRDD = getRDDStrings(sc,logFile)
	IDsRDD = getRDDStrings(sc,IDFile)
	alarmIDMappings = getDeviceManagedObjectsID(sc,alarmsRDD,IDsRDD)	
	print "\n\n\nThe Alarm mappings are:"
	print alarmIDMappings
	print "\n\n\n"
