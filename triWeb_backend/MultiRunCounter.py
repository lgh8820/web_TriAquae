#!/usr/bin/env python

import db_connector

from web01.models import OpsLog 


def AddNumber():
	current_num =  OpsLog.objects.latest('track_mark').track_mark #MultiRunCounter.objects.all()[0]
	new_num =  current_num + 1
	return new_num 

if __name__ == '__main__':
	print 'This module can not be run by it self,must be called by other programs.'
	print AddNumber()
