#Marc R. Miller
#Let's see where that International Space Station be, huh? REAL TIME! 

import sys
import Tkinter
import math
import time
from datetime import datetime
import ephem
 
degrees_per_radian = 180.0 / math.pi
 
home = ephem.Observer()
#22 Comares Ave lat and long coordinates
home.lon = '-81.29471'   # +E
home.lat = '29.89107'      # +N
#No elevation. We live on the fucking water, yo. 
home.elevation = 0 # meters
 
# Be sure to keep the ISS TLE data updated:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
    '1 25544U 98067A   16008.54515867  .00016717  00000-0  10270-3 0  9003',
    '2 25544  51.6413 139.1769 0008776  14.9781 345.1631 15.55285411 19994'
)
 
while True:
    home.date = datetime.utcnow()
    iss.compute(home)
    print('Altitude(above horizon): %4.1f deg, azimuth(clockwise from the North): %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
    time.sleep(1.0)

#gotEm.
