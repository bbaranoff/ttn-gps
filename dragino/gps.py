import json
# importing the module
import gpsd
from cayennelpp import LppFrame, LppUtil
# Connect to the local gpsd
gpsd.connect()
packet = gpsd.get_current()
frame = LppFrame()
# See the inline docs for GpsResponse for the available data
print(packet.position())
lat = packet.lat
lon = packet.lon
alt = packet.alt

print (lat, lon, alt)

frame.add_gps(1,lat, lon, alt)
print(json.dumps(frame, default=LppUtil.json_encode, indent=2))
