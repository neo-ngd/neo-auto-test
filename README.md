# neo-auto-test
to implement neo-cli auto test 

## preparation
1. install python3.7.0
2. install screen
3. install expect
4. download neo-cli-linux
5. authorize neo-cli excute permission
```
cd neo-cli
chmod +x ./neo-cli
```
6. completely synchonize neo-cli chain data

## configuration

```
{
    "neoclipath": "~/neo-cli",//neo-cli directory
    "interval": 10,//second, check interval
    "restartthreshold": 100,//whether to restart according how many blocks behind
    "startsilent": 60, //minute, least interval to restart
    "localsrv": "http://localhost:10332",  //rpc to get local node height
    "seeds": [
        "seed1.ngd.network:10332",
        "seed2.ngd.network:10332",
        "seed3.ngd.network:10332",
        "seed4.ngd.network:10332",
        "seed5.ngd.network:10332",
        "seed6.ngd.network:10332",
        "seed7.ngd.network:10332",
        "seed8.ngd.network:10332",
        "seed9.ngd.network:10332"  
    ]
}
```
