from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest

client = AcsClient(
   "LTAIPOMV2WHMs3Yd",
   "3ELBKI5xkWd46odCnqcEuIWD3fFZ9v",
   "cn-beijing"
);
import json
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(100)
request.set_accept_format('json')
result = json.loads(client.do_action(request)).get('Instances').get('Instance')

for line in result:
    # 另一种方法 print('过期时间', line.get('ExpiredTime'), end=',')
    print('实例Id', line['InstanceId'], end='|')
    print('创建时间', line['CreationTime'], end='|')
    print('过期时间', line['ExpiredTime'], end='|')
    print('CPU', str(line['Cpu']) + '核', end='|')
    print('内存', str(line['Memory']) + 'M', end='|')
    print('网络带宽', str(line['InternetMaxBandwidthOut']) + 'M', end='|')
    print('运行状态', line['Status'], end='|')
    print('内网IP', line['NetworkInterfaces']['NetworkInterface'][0]['PrimaryIpAddress'], end='|')
    print('公网IP', line['PublicIpAddress']['IpAddress'])