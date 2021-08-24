'''
Created on Aug 23, 2021

@author: pavel degtyarev
'''
import random
from flask import Flask
from flask_restful import Resource, Api
from urllib.parse import urlparse
import base64

app = Flask(__name__)
api = Api(app)

encoding = 'UTF-8';
#encoding = 'ascii';
urlMap = {}

'''
This code will need to have proper URL validation and error handling, and handling of query parameters/fragments
a URL passed to the service must be base64 UTF-8 encoded.
The urlMap needs some kind of persistence to survive restarts  

'''

class GetFullUrl(Resource):       
        
    def get(self, urlstr):
        print(urlstr)
        b64 = urlstr.encode(encoding)
        mb = base64.b64decode(b64)
        pe = mb.decode(encoding)
        print(pe)
        # o = urlparse(pe)
        # path = o.path
        # path = path[1:]        
        # scheme = o.scheme
        # netloc = o.netloc
        # print(path)
        # print(o)  
        # o = urlparse(path)
        # path = o.path     
        # print(path)
        # print(o)           
        # b64 = path.encode(encoding)
        # mb = base64.b64decode(b64)
        # pe = mb.decode(encoding)
        # o = urlparse(pe)
        # path = o.path 
        print(urlMap)    
        return {'url': urlMap[pe]}     

'''    
This code will need to have proper URL validation and error handling, and handling of query parameters/fragments
a URL must is passed to the service base64 encoded 
'''     
class GetShortUrl(Resource):   
    
    def get(self, urlsstr):
        print(urlsstr)
        b64 = urlsstr.encode(encoding)
        mb = base64.b64decode(b64)
        print(mb)
        pe = mb.decode(encoding)
        o = urlparse(pe)
        path = o.path
        path = path[1:]
        print(path)
        print(o)
        scheme = o.scheme
        netloc = o.netloc
        # b64 = path.encode(encoding)
        # mb = base64.b64encode(b64)
        # pe = mb.decode(encoding)        
        randV = random.randint(1, 9999)       
        r = scheme + "://" + netloc + "/" + str(randV)
        urlMap[r] = pe
        print(urlMap)
        return {'url': r}   
    
api.add_resource(GetFullUrl, '/getfullurl/<urlstr>') 
api.add_resource(GetShortUrl, '/getshorturl/<urlsstr>')    


if __name__ == '__main__':
    app.run(debug=True)
        
