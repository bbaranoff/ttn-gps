# ttn-gps
GPS Tracker with dragino rpi hat v1.4

And Raspberry Pi 4 Powered with 5V 4A

Install latest version of RaspiOS-lite via raspi-imager
On Ubuntu Host
```bash
sudo snap install rpi-imager
```
launch rpi-imager
select other debian
RaspiOS-lite (32-bits)
```
bash
sudo mount /dev/sdX1
cd /media/"username"/boot
touch ssh
chmod +x ssh
sudo mount /dev/sdX2
cd /media/"username"/rootfs
sudo touch ssh
sudo chmod +x ssh
sudo umount /dev/sdX2
sudo umount /dev/sdX1
```
On Raspbian
```bash
cd ttn-gps
sudo ./dragino-rpi4-tracker.sh
```
If you want already customized OS
https://drive.google.com/file/d/16UmfTRoSbkwJQ_ICBfQlRyjoRv7t4N-C/view?usp=sharing
