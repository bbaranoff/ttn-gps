# ttn-gps
Install latest version of RaspiOS-lite via raspi-imager
On Ubuntu Host
```bash
sudo snap install rpi-imager
sudo mount /dev/sdX1
cd /media/"username"/boot
touch ssh
chmod +x ssh
sudo mount /dev/sdX2
cd /media/"username"/rootfs
sudo touch ssh
sudo chmod +x ssh
cd ttn-gps
sudo ./dragino-rpi4-tracker.sh
````
