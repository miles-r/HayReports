# Miles Rollison
# 02-10-2020

import arrow
import subprocess
import urllib.request

today = arrow.utcnow().format('YYYY_MMM_DD')
logfile = open('Logs/logfile_' + today + '.log', 'w')

def logmsg(msg):
	logfile.write(arrow.utcnow().format() + '\t' + msg + '\n')

# Thu Feb 6, 2020
link = "https://www.ams.usda.gov/mnreports/gl_gr310.txt"

f = urllib.request.urlopen(link)

logmsg('requested ' + link)

file = f.read()
report = file.decode("ascii", "replace")

filename = report.partition(' ')[0]
date = report.partition('Thu ')[2][:12]

date = arrow.get(date.replace(',', '').rstrip().replace(' ', '-'), 'MMM-D-YYYY')

filename = "Reports/" + filename + '_' + str(date.year) + '_' + str(date.month) + '_' + str(date.day) + '.txt'

filename
outfile = open(filename, 'w')
outfile.write(report)
outfile.close()

logmsg('write to ' + filename)

logmsg('git commit')

subprocess.Popen( ['git', 'add', "Reports/"])
subprocess.Popen( ['git', 'add', "Logs/"])
subprocess.Popen( ['git', 'commit', '-m', 'Automatic commit from python script'])


logfile.close()
