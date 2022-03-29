#!/usr/bin/env python3
import gpsd
gpsd.connect()
packet = gpsd.get_current()
packet.position()
