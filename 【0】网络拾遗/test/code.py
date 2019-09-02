f = open('ngx.log')
res = {}
while True:
    line = f.readline()
    if line == '':
        break
    http_code = line.split()[8]
    if http_code not in res:
        res[http_code] = 1
    else:
        res[http_code] += 1

v = sorted(res.items(), key=lambda i:i[1], reverse=True)
print(v[0:10])
f.close()
