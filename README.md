# RaspberryPiPDU
Creating a camera solution for PDU

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

## Access files on Mac

### View files or execute scripts

Open terminal on Mac
```ssh pdu@dogmoves.local```

They will ask for a password. The password for this is "ebony"

### Copy files to Mac

```scp pdu@dogmoves:/home/pdu/record/2022-11-23-10:36/NV_7.mp4 /users/nidhi/Desktop```
