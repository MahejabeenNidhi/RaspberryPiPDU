# RaspberryPiPDU
Creating a camera solution for PDU

Update device

```sudo apt-get update```

```sudo apt-get upgrade -y```

## Enable legacy camera support

Needed for ribbon camera

```sudo raspi-config```

## Dependencies to install

```sudo pip install pirecorder```

```sudo pip install "picamera[array]"```

```sudo apt-get install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libatlas3-base libjasper-dev python3-pyqt5 -y```

```sudo pip install opencv-contrib-python==4.5.3.56```

```sudo apt-get install python3-opencv```

```sudo pip install imutils```

## Start python script at boot

1. Create a directory called record in the root directory
2. Download python script in the record directory, i.e. record.py
3. Open terminal, go to record directory

```cd record```

4. Create launcher shell

```nano launcher.sh```

5. This will launch an editor. Type in the following script

```
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pdu/record
sudo python record.py
cd /
```

6. Make the launcher script executable

```chmod 755 launcher.sh```

7. Test it. This should run the Python code

```sh launcher.sh```

8. Navigate back to home directory 

```cd```

9. Create a logs directory

```mkdir logs```

10. Add to Crontab. Type in

```sudo crontab -e```

11. Enter the line

```@reboot sh /home/pdu/record/launcher.sh >/home/pdu/logs/cronlog 2>&1```

12. Reboot to check

```sudo reboot```

If it doesn't work, check the log file

```cd logs```

```cat cronlog```


## Access files on Mac

### View files or execute scripts

Open terminal on Mac

```ssh pdu@dogmoves.local```

They will ask for a password.

### Copy files to Mac

```scp pdu@dogmoves:/home/pdu/record/2022-11-23-10:36/NV_7.mp4 /users/nidhi/Desktop```
