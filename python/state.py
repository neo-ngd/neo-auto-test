import commands

def getRss():
    state, output = commands.getstatusoutput('ps -ef -o pid -o rss -o size -o vsize -o sz -o comm | grep neo-cli | awk \'{print $2}\'')
    if state != 0:
        return -1
    return int(output)