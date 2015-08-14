Alarm Tracker

This is just a simple program that I wrote to try out PySpark and develop an application that used Apache Spark.
It does simple text parsing, string matching operations over data stored on RDDs.

********************************

OBJECTIVE:

Developed a simple program that can be used for efficient alarm 
tracking of jobs deployed on distributed systems. Used Apache Spark's 
Python APIs (PySpark) to efficiently identify service IDs of the jobs 
that gave out alarms. Subsequently, since a map of alarm message 
serial number to service ID is obtained, further action can be taken 
with respect to that job.

********************************

DESCRIPTION:

1.	Large number of alarms are input as XML entries:

2.	Huge number of IDs (millions of strings) are also input.

3.	For each alarm, go through the list of IDs and try to find some 
	matching ID in the “device” or “managed-object” fields. 
	If any ID matches, go on to the next alarm.

4.	Apache Spark is used to carry out efficient string matching and 
	log parsing.

********************************

PREREQUISITES:

1.	Install Scala and Apache Spark According to the following 
	instructions: 
	http://stackoverflow.com/questions/31594937/error-invalid-or-corrupt-jarfile-sbt-sbt-launch-0-13-5-jar

2. Python 2

3. PySpark 

********************************

FILES:

1. spark_parser.py

	DESCRIPTION:

	-Parse Alarms to find the service ID that each alarm corresponds to 
	 using Pyspark which is the Python implementation for Apache Spark 
	 APIs. This program will return a hashmap with keys as the alarm 
	 number and value as the matching ID. Correspondingly, action can 
	 be taken on those serviceIDs.

 	-The 'SPARK_HOME' environment variable defines the location of the 
	 Apache Spark installation. The pyspark utility can be found at:
	 $SPARK_HOME/bin/pyspark


	EXECUTION:

 	-To run this program, give the following command to submit the 
  	 Apache Spark job:
  	 "$SPARK_HOME/bin/spark-submit  <this file>"

 	-Set the Alarms file location in the "logFile" variable as an HDFS 
	 URI or local file. The ID list against which to be matched can be 
	 provided in the "IDFile" variable. 
	
 	-To deploy on a cluster instead of a local machine, make changes to
  	 SparkConf() parameters.


	RESOURCES:
	-pyspark API Documentation: 
	 https://spark.apache.org/docs/latest/api/python/
  	 This URL will be referred to as "API_DOCs".

 	-Explanation of pySpark APIs used:

		SparkConf():
		Configuration for a Spark application. Used to set various Spark 
		parameters as key-value pairs. For more info, see:
		"API_DOCS"/pyspark.html?highlight=sparkconf#pyspark.SparkConf

		SparkContext():
		The main entry point for Spark functionality and it 
		represents the connection to a Spark cluster, 
		and can be used to create an RDD and broadcast variables 
		on that cluster.

		textFile():
		This  method will read a text file from HDFS, a local file 
		system (available on all nodes), or any Hadoop-supported 
		file system URI, and return it as an RDD of Strings.

		cache():
		This method is used to persist this RDD with the default 
		storage level (MEMORY_ONLY_SER).

2. XML_Parsing/xml_parser.py

	DESCRIPTION:
	This simple program is used to parse XML alarm files, extract
	the device and managed-object fields from an alarm message
	and then find a matching ID from a list of IDs. This is the
	basic XML parsing program written to extract IDs without using
	PySpark.

	EXECUTION:
	To run execute:
	"python <python file>"

3. XML_Parsing/sample_alarms.xml
	
	DESCRIPTION:
	Sample XML file containing the alarms that are output by various
	jobs running on the cluster.

4. XML_Parsing/sample_IDs.txt

	DESCRIPTION:
	Sample text file containing a small number of ID strings to match.

********************************

CREATED BY:

Chinmay Kulkarni

********************************
