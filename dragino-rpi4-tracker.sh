#!/bin/bash
sudo apt update && sudo apt upgrade
sudo apt install git device-tree-compiler git python3-crypto python3-nmea2 python3-rpi.gpio python3-serial python3-spidev python3-configobj gpsd libgps-dev gpsd-clients libgps23
gcc coordinates.c -o coordinates -lm -lgps
cp coordinates /home/pi/coordinates
sudo cp config.txt /boot/config.txt
sudo cp cmdline.txt /boot/cmdline.txt
sudo cp gpsd /etc/default/gpsd
cd dragino/overlay
sudo dtc -@ -I dts -O dtb -o spi-gpio-cs.dtbo spi-gpio-cs-overlay.dts
sudo cp spi-gpio-cs.dtbo /boot/overlays/
sudo reboot
