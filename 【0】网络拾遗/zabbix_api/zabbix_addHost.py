import zabbix_base
token = zabbix_base.get_token()
hostname='zabbixapihost'
hostip = '192.168.232.128'
groupid = 16
templateid="10001"
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": hostname,
        "interfaces": [{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": hostip,
            "dns": "",
            "port": "10050"
        }],
        "groups": [{
            "groupid": groupid
        }],
        "templates": [{
        "templateid": templateid
        }],
    },
    "auth": token,
    "id": 1
}
result = zabbix_base.zabbix_api_common(data)
print(result)