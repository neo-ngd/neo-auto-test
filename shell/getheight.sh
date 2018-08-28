#!/usr/bin/expect -f
set timeout -1
set neoclipath [lindex $argv 0]
cd $neoclipath

spawn screen -r neo-cli

expect "neo>"

send "\01"
send "d"