#!/usr/bin/python
#	DESCRIPTION:
#	This program is used to parse XML alarm files and 
#	check the device and managed-object fields of each
#	alarm entry against a list of IDs.
#
#	EXECUTION:
#	To run execute:
#	python <python file>
#
#	CREATED BY:
#	Chinmay Kulkarni

import xml.etree.cElementTree as ET
#Global Vaiables
alarmLogFile = "sample_alarms.xml"
IDFile = "sample_IDs.txt"

#Goes through the list of IDs and finds a matching ID in device or managed
#Objects fields.
def getID(IDFile,device,mgdObj):
	IDs = open(IDFile,'r')
	for line in IDs:
		line = line.strip()
		if line in device or line in mgdObj:
			return line


#Right now condsidering that there is just one alarm in the xml file.
def parseXML(xmlFileName):
	tree = ET.ElementTree(file=xmlFileName)
	root = tree.getroot()
	alarmNoti = ""
	lengthCommonString = 0
	for child in root:
		tag = child.tag
		if tag.endswith("alarm-notification"):
			lengthCommonString = len(tag) - 18
			alarmNoti = child
			break
	device = ""
	managedObj = ""
	found = 0
	for element in alarmNoti:
		tag = element.tag[lengthCommonString:]
		if tag == "device":
			device = element.text
			found += 1	
		if tag == "managed-object":
			managedObj = element.text
			found += 1	
		if found == 2:
			break
	return device,managedObj


if __name__ == "__main__":
	device, mgdObj = parseXML(alarmLogFile)
	print device,"\t",mgdObj
	alarmID = getID(IDFile,device,mgdObj)
	print "Found Alarm ID\t:",alarmID
	print "In alarm entry:\tdevice= ",device,"\tmanagedObject = ", mgdObj

