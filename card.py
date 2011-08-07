import json
import urllib2
import commands
import time

interval = 60 #interval in seconds
duration = 3 #duration of check in hours
threshold = 50.0 #alert threshold
n = 0

while n < (duration*60*60/interval):
    result = json.loads(urllib2.urlopen('http://jonathanstark.com/card/api/latest').read())
    balance = float(result['balance']['amount'])
    n += 1
    if balance > threshold:
        commands.getstatusoutput('open ./play.app') #Play your iTunes library
    else:
        print "%s is not over %s" % (balance, threshold)
    time.sleep(interval)
