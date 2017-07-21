from gpiozero import LED, Button
from signal import pause
import urllib2

Led = LED(17)
bitton = button(2)

def ifttt():
    print "done"
    urllib2.urlopen("https://maker.ifttt.com/trigger/button_press/with/key/07rT$
button.when_presssed = ifttt
pause()



