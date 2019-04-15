import time
import datetime
from envirophat import light, motion, weather, leds
out = open('/var/www/html/scripts/enviro.csv', 'a')
lux = light.light()
# leds.on()
# rgb = str(light.rgb())[1:-1].replace(' ', '')
# leds.off()
# acc = str(motion.accelerometer())[1:-1].replace(' ', '')
# heading = motion.heading()
temp = weather.temperature()
temp = 9.0/5.0 * temp + 32
temp = temp - 7
press = weather.pressure()
timestamp = datetime.datetime.now().isoformat()
out.write('%f,%s,%f,%f\n' % (lux, timestamp, temp, press))
out.close()
