#!/usr/bin/env python3
# Solstice OpenControl API -  WiFi Password Change Demo

# Please modify this to use your own values for Pod IP, ssid and password

# Note that for the wifiConfig setting to work, all values must be set
# and posted back to the pod. The easiest way to do this is to read the
# wifiConfig values from the pod and reuse them.

# Also note that since the password is always returned as '*', it must be set
# to the real password if you set other values.

import requests

# If the pods have administrator passwords. Otherwise leave this empty.
admin_password = ''

def get_config(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def set_config(url, config):
    response = requests.post(url, json=config)
    response.raise_for_status()

def set_wifi(ip):
    config_url = 'http://'+ip+'/api/config'
    if(admin_password):
            config_url += '?password='+admin_password

    config = get_config(config_url)
    print(config['m_networkCuration']['wifiConfig'])

    # We do not copy all of the config settings. Only the wifiConfig is needed.
    new_config = {'m_networkCuration': 
        {'wifiConfig': config['m_networkCuration']['wifiConfig']}
    }
    new_config['m_networkCuration']['wifiConfig']['ssid']     = 'Guest'
    new_config['m_networkCuration']['wifiConfig']['password'] = ''
    set_config(config_url, new_config)

# A list of IP addresses or hostnames.
# All of them will be changed.
ips = [
    '192.168.3.175',
]

for ip in ips:
    set_wifi(ip)

exit()
