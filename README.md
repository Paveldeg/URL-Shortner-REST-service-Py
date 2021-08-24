# URL-Shortner-REST-service-Py
basic URL shortener RESTfull service using Flask, tested with Python 3.9.0

How to run:
py UrlShortnerSrv.py

How to use:
1. to get shortened version of a URL - Invoke "http://127.0.0.1:5000/getshorturl/[url]" from a browser, 
substitute [url] with a BASE64 UTF-8 encoded URL.

Sample req/response:
http://127.0.0.1:5000/getshorturl/aHR0cHM6Ly9teWhvc3Q6ODA4MC8vcnRyL3J0eXJ0eS9yZXRldGV0ZWUvNDU2NDU2NC80NTY0NjQ1NjUzNDM0

{
    "url": "https://myhost:8080/2378"
}

 
2. to get full version of a shortened URL - Invoke "http://127.0.0.1:5000/getfullurl/[url]" from a browser, 
substitute [url] with a BASE64 UTF-8 encoded URL from above response.

Sample req/response:
http://127.0.0.1:5000/getfullurl/aHR0cHM6Ly9teWhvc3Q6ODA4MC8yMzc4Cg==

{
    "url": "https://myhost:8080//rtr/rtyrty/retetetee/4564564/4564645653434"
}

