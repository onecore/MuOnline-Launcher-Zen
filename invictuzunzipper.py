import zipfile
import subprocess
import sys
import urllib2
import time
__author__ = 'Mark Pequeras'

opentoUnzip = open('verzip.py','r+')
subprocess.Popen('taskkill /f /im LauncherNew.exe')
sys.stderr = open('InvictuzError.log','w')
sys.stdout = open('InvictuzOut.log','w')

CSunzip = zipfile.ZipFile(r'+'+str(opentoUnzip)+'.zip'+'+')
print CSunzip
#CSunzip.extractall(r'')

sys.exit(0)