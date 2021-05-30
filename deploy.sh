#!/bin/bash
set -x
PI_IP=192.168.0.12
USER=root
UTIL=/root/util
ssh $USER@$PI_IP mkdir -p $UTIL
scp ./*.py $USER@$PI_IP:$UTIL
ssh $USER@$PI_IP python $UTIL/avrcp_manager