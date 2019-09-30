import zabbix_base
token = zabbix_base.get_token()
groupname = "shijiangeapigroup"
data={
  "jsonrpc": "2.0",
  "method": "hostgroup.create",
  "params": {
    "name": groupname
  },
  "auth": token,
  "id": 1
}
result = zabbix_base.zabbix_api_common(data)
print(result)

