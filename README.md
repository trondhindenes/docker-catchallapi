# docker-catchallapi

Simple rest api which responds with lots of information about the incoming request. Use it to troubleshoot/test microservice routing and other things.
By default it listens on port 80, can be overriden by setting the LISTEN_PORT environment variable.

### Supported http methods:
GET and POST

### Get it on docker hub:
https://hub.docker.com/r/trondhindenes/docker-catchallapi/

### Supported things:
- path
- query string
- body (POST)

Note that for http post, the `request.json_body` uses flasks `request.json` object, which will only be filled if content-type is set to `application/json`.

Examples:

Request: 
```
curl http://localhost:9000/shoes/stuff
```

Response:
```json
{
    "path": "/shoes/stuff",
    "local_computer_name": "e5ba71237589",
    "headers": {
        "HTTP_ACCEPT": "*/*",
        "HTTP_USER_AGENT": "PostmanRuntime/7.2.0",
        "HTTP_CONNECTION": "keep-alive",
        "SERVER_PORT": "80",
        "SERVER_NAME": "0.0.0.0",
        "HTTP_POSTMAN_TOKEN": "781b8481-db5c-4e4e-aa77-79cc801cfff0",
        "REMOTE_PORT": "55352",
        "SERVER_SOFTWARE": "CherryPy/17.3.0 Cheroot/6.4.0 Server",
        "SCRIPT_NAME": "",
        "HTTP_ACCEPT_ENCODING": "gzip, deflate",
        "ACTUAL_SERVER_PROTOCOL": "HTTP/1.1",
        "REQUEST_METHOD": "GET",
        "HTTP_HOST": "localhost:9000",
        "PATH_INFO": "/shoes/stuff",
        "CONTENT_TYPE": "application/json",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "QUERY_STRING": "",
        "HTTP_CACHE_CONTROL": "no-cache",
        "REMOTE_ADDR": "172.17.0.1",
        "REQUEST_URI": "/shoes/stuff"
    }
}
```

Request: 
```curl -X POST \
  'http://localhost:9000/snakkes?what=true&stuff=njet' \
  -H 'Content-Type: application/json' \
  -d '{
	"stuff": "good"
}'
```

Response:
```json

{
    "path": "/snakkes",
    "local_computer_name": "e5ba71237589",
    "request": {
        "values": {},
        "json_body": {
            "stuff": "good"
        }
    },
    "headers": {
        "HTTP_ACCEPT": "*/*",
        "CONTENT_LENGTH": "20",
        "HTTP_USER_AGENT": "PostmanRuntime/7.2.0",
        "HTTP_CONNECTION": "keep-alive",
        "SERVER_PORT": "80",
        "SERVER_NAME": "0.0.0.0",
        "HTTP_POSTMAN_TOKEN": "48ecd7bf-6532-4a2a-9804-c7659a21947d",
        "REMOTE_PORT": "55386",
        "SERVER_SOFTWARE": "CherryPy/17.3.0 Cheroot/6.4.0 Server",
        "SCRIPT_NAME": "",
        "HTTP_ACCEPT_ENCODING": "gzip, deflate",
        "ACTUAL_SERVER_PROTOCOL": "HTTP/1.1",
        "REQUEST_METHOD": "POST",
        "HTTP_HOST": "localhost:9000",
        "PATH_INFO": "/snakkes",
        "CONTENT_TYPE": "application/json",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "QUERY_STRING": "what=true&stuff=njet",
        "HTTP_CACHE_CONTROL": "no-cache",
        "REMOTE_ADDR": "172.17.0.1",
        "REQUEST_URI": "/snakkes?what=true&stuff=njet"
    }
}
```