import pymongo
from pymongo import MongoClient
client = MongoClient('192.168.174.128', 27017)
print(client)