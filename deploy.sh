#!/bin/bash
set -x
PI_IP=${1:-192.168.1.12}
scp ./*.py root@$PI_IP:/root/util
ssh root@$PI_IP python /root/util/__init__.py