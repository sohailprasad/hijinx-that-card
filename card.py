import json
import urllib2
import commands
import time

interval = 60 #interval in seconds
duration = 3 #duration of check in hours
threshold = 50.0 #alert threshold
n = 0

while n < (duration*60*60/interval):
    try:
        result = json.loads(urllib2.urlopen('http://jonathanstark.com/card/api/latest').read())
    except:
        print "Error loading resource."
        commands.getstatusoutput('open ./play.app') #Play your iTunes library
    balance = float(result['balance']['amount'])
    n += 1
    if balance > threshold:
        commands.getstatusoutput('open ./play.app') #Play your iTunes library
        print "BALANCE IS %s" % balance
    else:
        print "%s is not over %s" % (balance, threshold)
    time.sleep(interval)
