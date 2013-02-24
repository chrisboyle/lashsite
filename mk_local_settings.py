#!/usr/bin/env python

import random

secret = ("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))

with open('local_settings.py','w') as f:
	f.write("DEBUG = True\nSECRET_KEY = \"%s\"\n" % secret)
