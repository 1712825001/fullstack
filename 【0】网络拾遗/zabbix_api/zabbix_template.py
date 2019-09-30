import zabbix_base

token = zabbix_base.get_token()
data = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": ["host"],
    },
    "auth": token,
    "id": 1
}
result = zabbix_base.zabbix_api_common(data)
for i in result['result']:
    print(i)
