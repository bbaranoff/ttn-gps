from cayenneLPP import CayenneLPP

# creating Cayenne LPP packet
lpp = CayenneLPP()

# adding 2 digital outputs, the first one uses the default channel
lpp.addGPS(3, 52.37365, 4.88650, 2);
