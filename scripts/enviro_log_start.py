#make new csv w/ headers
out = open('/var/www/html/scripts/enviro.csv', 'w')
out.write('light,timestamp,temp,press\n')
out.close()
out = open('/var/www/html/scripts/outside_temp.csv', 'w')
out.write('timestamp,tempOut\n')
out.close()
