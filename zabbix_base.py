import json
from urllib import request
zabbix_url="http://192.168.232.128/zabbix/api_jsonrpc.php"
zabbix_header = {"Content-Type":"application/json"}

def get_token():
    zabbix_user   = "Admin"
    zabbix_pass   = "Feng1han"
    data = {
      "jsonrpc":"2.0",
      "method":"user.login",
      "params":{
        "user":zabbix_user,
        "password":zabbix_pass
      },
      "id":0
    }
    result = zabbix_api_common(data)
    return result['result']

def zabbix_api_common(data):
    data = json.dumps(data).encode('utf-8')
    req = request.Request(zabbix_url, headers=zabbix_header, data=data)
    result = request.urlopen(req).read()
    return json.loads(result)

if __name__ == "__main__":
    result = get_token()
    print(result)


