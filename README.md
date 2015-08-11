# Alarm_Tracker
Alarm Tracker 

TODO:

1.	Large number of alarms are input in the following format:
<notification
    xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
    <eventTime>2015-07-10T16:12:29.992497+00:00</eventTime>
    <alarm-notification
        xmlns="http://tail-f.com/ns/ncs-alarms">
        <alarm-class>new-alarm</alarm-class>
        <device>SKT-3-vinay02-SKT-CSR-esc-vz</device>
        <type>ned-live-tree-connection-failure</type>
        <managed-object>snmp</managed-object>
        <specific-problem/>
        <event-type>communicationsAlarm</event-type>
        <has-clear>true</has-clear>
        <kind-of-alarm>root-cause</kind-of-alarm>
        <probable-cause>0</probable-cause>
        <event-time>2015-07-10T16:12:29.986535+00:00</event-time>
        <perceived-severity>major</perceived-severity>
        <alarm-text>Connection to SKT-3-vinay02-SKT-CSR-esc-vz timed out</alarm-text>
    </alarm-notification>
</notification>

2.	Huge number of IDs (millions of strings) are also input. 

3.	For each alarm, go through the list of IDs and try to find some matching ID
	in the “device” or “managed-object” fields. If any ID matches, go on to 
	the next alarm.
4.	Try to leverage Apache storm/spark for this to make it distributed or 
	faster. 
5.	Eventually, try to learn patterns (location where the “ID” matches in the 
	alarms) so that you don’t need to perform this expensive search in each 
	alarm message. 	


******
Install Scala and Apache Spark According to the following instructions:
http://stackoverflow.com/questions/31594937/error-invalid-or-corrupt-jarfile-sbt-sbt-launch-0-13-5-jar
