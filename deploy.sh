#!/bin/bash
scp ./* root@192.168.1.12:/root/util
ssh root@192.168.1.12 python /root/util/__init__.py