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

#how mand blocks behind the best block count
RESTART_THRESHOLD = 100
#avoid restarting within the time after start
START_RECENTLY = 60
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
    logging.info('[getBestBlockCount] maxheight: {0}'.format(maxHeight))
    return maxHeight

def getLocalBlockCount():
    height = neoapi.getCurrentHeight(LOCAL_SRV)
    logging.info('[getLocalBlockCount] localheight: {0}'.format(height))
    return height

def isLocalRunning():
    (state, output) = commands.getstatusoutput('ps -ef | grep "./neo-cli" | wc -l')
    logging.info('[isLocalRunning] shell command, state: {0}, output: {1}'.format(state, output))
    if state != 0:
        height = getLocalBlockCount()
        logging.info('[isLocalRunning] command failed, use rpc getblockcount. height: {0}'.format(height))
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
    if timedelta(minutes=START_RECENTLY) < datetime.now() - lastRestartTimestamp:
        return True
    return False

while True:
    if not isLocalRunning():
        startLocalNode()
        continue
    localBlockCount = getLocalBlockCount()
    bestBlockOount = getBestBlockCount()
    if RESTART_THRESHOLD < bestBlockOount - localBlockCount and not restartRecently():
        restart_cnt += 1
        logging.warning('[restart] restarting, restart_cnt: {0}, localheight: {1}, bestheight: {2}'.format(restart_cnt, localBlockCount, bestBlockOount))
        stopLocalNode()
        startLocalNode()
    time.sleep(5 * 60)