#!/usr/bin/env hpython

import hstub
import time
from os import environ

from statsd import statsd
from hermes.pages.scoreboard import readScoreboard
from os import environ

if environ.get('HTTP_X_FORWARDED_FOR') == '209.234.129.174':
    _start = time.time()

    completes3m = readScoreboard(25000,180)[5]

    countPerSecond = int(completes3m / 180)

    statsd.gauge('scripts.completes.completes3m', int(completes3m))


    print "Content-type:text/html\r\n\r\n"
    print '<html>'
    print '<head>'
    print '<title>Completions</title>'
    print '</head>'
    print '<body>'
    print 'Completes in last 3 minutes: ' + str(completes3m)
    print '<br/>'
    print 'Average completes per second in last 3 minutes: ' + str(countPerSecond)
    print '</body>'
    print '</html>'

    duration = time.time() - _start

    statsd.histogram('scripts.completes.cgiTime', duration)



else:
    print 'Content-type:text/html\r\n\r\n'
    print '<html>'
    print '<head>'
    print '<title>Access Denied</title>'
    print '</head>'
    print '<body>'
    print 'ACCESS DENIED - INVALID IP ADDRESS'
    print '</body>'
    print '</html>'

