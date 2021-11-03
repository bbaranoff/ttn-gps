#!/bin/bash
sudo apt install device-tree-compiler git python3-crypto python3-nmea2 python3-rpi.gpio python3-serial python3-spidev python3-configobj
sudo cp config.txt /boot/config.txt
sudo cp cmdline.txt /boot/cmdline.txt
cd dragino/overlay
sudo dtc -@ -I dts -O dtb -o spi-gpio-cs.dtbo spi-gpio-cs-overlay.dts
sudo cp spi-gpio-cs.dtbo /boot/overlays/
sudo reboot
