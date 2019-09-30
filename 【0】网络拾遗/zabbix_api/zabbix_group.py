import zabbix_base
token = zabbix_base.get_token()
data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    # "params": {
    #     # "output": "extend",
    #     "output": "name",
    #     "filter":{
    #         "name":[
    #             "web"
    #         ]
    #     }
    # },
    "params": {
        "output": ['name'],
        "selectHosts": ["host"],
    },

    "auth": token,
    "id": 0
}
result = zabbix_base.zabbix_api_common(data)
print(result)


