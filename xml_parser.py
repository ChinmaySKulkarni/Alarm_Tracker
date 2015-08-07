#!/usr/bin/python
#	This program is used to parse XML alarm files and 
#	check the device and managed-object fields of each
#	alarm entry against a list of IDs.
#
#	Developed by: Chinmay Kulkarni

import xml.etree.cElementTree as ET
#Global Vaiables
alarmLogFile = "sample_alarms.xml"


def parseXML(xmlFileName):
	tree = ET.ElementTree(file=xmlFileName)
	root = tree.getroot()
	device = ""
	managed_obj = ""
	found = 0
	for child in root:
		print child.name
	print "\n\n\n\n"
	for element in tree.iter():
		tag = element.tag
		print element, tag
		if tag.endswith("device"):
			device = element.text
			found += 1
		if tag.endswith("managed-object"):
			managed_obj = element.text
			found += 1
		if found == 2:
			break
	print device
	print managed_obj
	
def tryP(n):
	tree = ET.ElementTree(file=n)
	root = tree.getroot()
	alarmNoti = ""
	lengthCommonString = 0
	for child in root:
		tag = child.tag
		if tag.endswith("alarm-notification"):
			lengthCommonString = len(tag) - 18
			alarmNoti = child
			break
	for element in alarmNoti:
		print element.tag[lengthCommonString:]	


if __name__ == "__main__":
	#parseXML(alarmLogFile)
	tryP(alarmLogFile)


