#!/bin/bash
set -x
PI_IP=192.168.1.12
USER=pi
UTIL=/home/pi/util
ssh $USER@$PI_IP mkdir -p $UTIL
scp ./*.py $USER@$PI_IP:$UTIL
ssh $USER@$PI_IP python $UTIL/avrcp_manager