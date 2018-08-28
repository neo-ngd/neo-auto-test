#!/usr/bin/expect -f
set timeout -1
set neoclipath [lindex $argv 0]
cd $neoclipath

spawn screen -S neo-cli ./neo-cli -r

expect "neo>"

# Insert here your wallet path
#send "open wallet /home/consensus/cn_wallet.json\n"

#expect "password:"

# Insert here your wallet password
#send "SOMESTRONGPASSWORD\n"

#expect "neo>"
#send "start consensus\n"
#expect "OnStart"
send "\01"
send "d"
