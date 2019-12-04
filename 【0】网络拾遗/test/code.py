# 统计nginx日志
# f = open('ngx.log')
# res = {}
# while True:
#     line = f.readline()
#     if line == '':
#         break
#     http_code = line.split()[8]
#     if http_code not in res:
#         res[http_code] = 1
#     else:
#         res[http_code] += 1
#
# v = sorted(res.items(), key=lambda i:i[1], reverse=True)
# print(v[0:10])
# f.close()

ip_count = {}
with open('ngx.log') as f:
    lines = f.readlines()

for line in lines:
    ip = line.split()[0]

    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1
print(ip_count)
#print(ip_count.items())
for ip, count in sorted(ip_count.items(), key=lambda x:x[1], reverse=True):
    print(f'{ip} -- {count}')


