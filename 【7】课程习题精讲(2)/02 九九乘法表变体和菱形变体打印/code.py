from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
# 创建AcsClient实例
client = AcsClient(
   "LTAIPOMV2WHMs3Yd",
   "3ELBKI5xkWd46odCnqcEuIWD3fFZ9v",
   "cn-beijing"
);
# 创建request，并设置参数
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(30)
# 发起API请求并显示返回值
response = client.do_action_with_exception(request)
#print(response)

import json
t = json.loads(response)

for k,v in t.items():
   print(k, v)

t1 = t['Instances']['Instance']
for v in t1:
   print(v)

import subprocess
print(subprocess.getoutput('ls -al'))
