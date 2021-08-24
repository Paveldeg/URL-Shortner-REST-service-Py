'''
Created on Aug 23, 2021

@author: pavel degtyarev
'''
#import requests
from flask import Flask
from flask_restful import Resource, Api
from urllib.parse import urlparse
import base64


app = Flask(__name__)
api = Api(app)

'''
This code will need to have proper URL validation and error handling, and handling of query parameters/fragments
a URL must is passed to the service base64 encoded  
'''

class GetFullUrl(Resource):       
        
    def get(self, urlstr):
        print(urlstr)
        b64 = urlstr.encode('UTF-8')
        mb = base64.b64decode(b64)
        pe = mb.decode('UTF-8')
        o = urlparse(pe)
        path = o.path
        path = path[1:]        
        scheme = o.scheme
        netloc = o.netloc
        print(path)
        print(o)  
        o = urlparse(path)
        path = o.path     
        print(path)
        print(o)           
        b64 = path.encode('UTF-8')
        mb = base64.b64decode(b64)
        pe = mb.decode('UTF-8')
        o = urlparse(pe)
        path = o.path 
        print(path)    
        return {'url': scheme + "://" + netloc + "/" + path}     

'''    
This code will need to have proper URL validation and error handling, and handling of query parameters/fragments
a URL must is passed to the service base64 encoded 
'''     
class GetShortUrl(Resource):   
    
    def get(self, urlsstr):
        print(urlsstr)
        b64 = urlsstr.encode('UTF-8')
        mb = base64.b64decode(b64)
        print(mb)
        pe = mb.decode('UTF-8')
        o = urlparse(pe)
        path = o.path
        path = path[1:]
        print(path)
        print(o)
        scheme = o.scheme
        netloc = o.netloc
        b64 = path.encode('UTF-8')
        mb = base64.b64encode(b64)
        pe = mb.decode('UTF-8')
        return {'url': scheme + "://" + netloc + "/" + pe}   
    
api.add_resource(GetFullUrl, '/getfullurl/<urlstr>') 
api.add_resource(GetShortUrl, '/getshorturl/<urlsstr>')    


if __name__ == '__main__':
    app.run(debug=True)
        