import redis
redisArgs={
    'host':'192.168.174.128',
    'port':6379,
    'password':'',
}
re = redis.Redis(**redisArgs)
print(re)

re.set('k1', '赵冬梅')
print(re.get('k1').decode('utf8'))
