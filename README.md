# homebridge_huum_wrapper
HomeBridge HUUM.EU API wrapper


Usage
=============
Crate virtual env

``mkdir homebridge_huum_wrapper && cd homebridge_huum_wrapper && python3 -m venv ./``

Clone the repository

```
git clone https://github.com/kepsic/homebridge_huum_wrapper
cd homebridge_huum_wrapper
../bin/python3 setup.py install
```

Replace in homebridge_huum_wrapper.ini with your corresponding username and password as used in HUUM.EU app

```
huum.username = username@example.com
huum.password = my_secret_password
```

Start wrapper
```
../bin/pserve homebridge_huum_wrapper.ini&
```

or with script
```
./start.sh&
```


Follow the HomeBridge Installation [manual](https://github.com/homebridge/homebridge/wiki/Install-Homebridge-on-Raspbian)

From plugins section install ``homebridge-thermostat``

Append thermostat into accessories section


```json
        {
            "accessory": "Thermostat",
            "name": "Sauna",
            "apiroute": "http://localhost:6543",
            "maxTemp": 110,
            "minTemp": 40,
            "model": "Sauna",
            "manufacturer": "HUUM"
        },
```
