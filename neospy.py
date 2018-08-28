import sys
import os
sys.path.append('./')
from config import config

print(config['neoclipath'])

result = os.system('./shell/start.sh {0}'.format(config['neoclipath']))
print('start result: ', result)