import subprocess
import time
import datetime
import re
out = open('/var/www/html/scripts/outside_temp.csv', 'a')
result = subprocess.run(['curl', 'wttr.in?format="%t"'], stdout=subprocess.PIPE)
result=result.stdout.decode('utf-8')
#find digits with optional pos/neg notation
re.findall(r'[-+]?\d+',result)
tempOut=result
timestamp = datetime.datetime.now().isoformat()
out.write('%s,%s' % (timestamp,tempOut))
out.close()
