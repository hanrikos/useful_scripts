#!/usr/bin/env python

# Description	: Maps DNS from a given domain.

import socket
import sys

domain = raw_input("Enter domain: ")
 
try:
    ip = socket.gethostbyname(domain)
 
except socket.gaierror:
    print "Invalid Domain: " + domain
    sys.exit()
print "DNS: " + ip