#!/usr/bin/python
#	This program is used to parse XML alarm files and 
#	check the device and managed-object fields of each
#	alarm entry against a list of IDs.
#
#	Developed by: Chinmay Kulkarni

import xml.etree.cElementTree as ET
#Global Vaiables
alarmLogFile = "sample_alarms.xml"

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
	print device
	print managedObj

if __name__ == "__main__":
	parseXML(alarmLogFile)


