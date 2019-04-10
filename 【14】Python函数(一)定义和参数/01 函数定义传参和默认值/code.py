def login(host='127.0.0.1', port='8080', username='wayne', password='magedu'):
    print('{}:{}@{}/{}'.format(host, port, username, password))

login()
login('127.0.0.1', 80, 'tom', 'tom')
login('127.0.0.1', username='root')
login('localhost', port=80, password='com')
login(port=80, password='magedu', host='www')