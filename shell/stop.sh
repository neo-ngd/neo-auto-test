#!/usr/bin/expect -f
set timeout -1

spawn screen -r neo-cli
sleep 2
expect "neo>"

# Insert here your wallet path
#send "open wallet /home/consensus/cn_wallet.json\n"

#expect "password:"

# Insert here your wallet password
#send "SOMESTRONGPASSWORD\n"

#expect "neo>"
#send "start consensus\n"
#expect "OnStart"
send "exit\r"
expect eof