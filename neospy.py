import sys
import os
import time
import commands
from datetime import datetime, timedelta
sys.path.append('./')
from config import config
sys.path.append('./python/')
import neoapi
from log import logging

RESTART_THRESHOLD = 100
RESTART_RECENTLY = 60
LOCAL_SRV = 'http://localhost:10332'
lastRestartTimestamp = datetime.now()
restart_cnt = 0

def getBestBlockCount():
    maxHeight = -1
    for seed in config['seeds']:
        logging.info(seed)
        height = neoapi.getCurrentHeight('http://' + seed)
        logging.info(height)
        if maxHeight < height:
            maxHeight = height
    return maxHeight

def getLocalBlockCount():
    height = neoapi.getCurrentHeight(LOCAL_SRV)
    return height

def isLocalRunning():
    (state, output) = commands.getstatusoutput('ps -ef | grep "./neo-cli" | wc -l')
    if state != 0:
        height = getLocalBlockCount()
        if height < 0:
            return False
        return True
    if int(output) <= 2:
        return False
    return True

def startLocalNode():
    result = os.system('./shell/start.sh {0}'.format(config['neoclipath']))
    if result == 0:
        global lastRestartTimestamp 
        lastRestartTimestamp = datetime.now()
        return True
    return False

def stopLocalNode():
    result = os.system('./shell/stop.sh')
    if result == 0:
        return True
    os.system('ps -ef | grep "./neo-cli" | awk \'{print $2}\' | xargs kill')
    return True

def restartRecently():
    if timedelta(minutes=60) < datetime.now() - lastRestartTimestamp:
        return True
    return False

while True:
    if not isLocalRunning():
        startLocalNode()
        continue
    localBlockCount = getLocalBlockCount()
    bestBlockOount = getBestBlockCount()
    if 100 < bestBlockOount - localBlockCount and not restartRecently():
        restart_cnt += 1
        logging.warning('[restart] restarting {0}'.format(restart_cnt))
        stopLocalNode()
        startLocalNode()
    time.sleep(5 * 60)