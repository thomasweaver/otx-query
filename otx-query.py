#!/usr/bin/python
from OTXv2 import OTXv2
import re


fh = open('apikey.token', 'r')
key = fh.read()
key = key.rstrip()

reg=re.compile('^[a-z0-9\.]+$')
if not (reg.match(key)):
    print "Key can only contain alphanumeric characters"
    exit(1)

#print key
otx = OTXv2(key)
indicators = otx.get_pulse_indicators("5952c2aaa533a362fb0d09d3")
for indicator in indicators:
    print indicator["indicator"] + "   " + indicator["type"]
