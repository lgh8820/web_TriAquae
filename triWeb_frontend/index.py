#-*- coding:utf-8 -*-
import os
import sys
'''
for running from bae
will sync by git hook
'''
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'TriAquae.settings'
 
path = os.path.dirname(os.path.abspath(__file__)) + '/TriAquae'
if path not in sys.path:
    sys.path.insert(1, path)
 
from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication
 
application = WSGIApplication(WSGIHandler())
