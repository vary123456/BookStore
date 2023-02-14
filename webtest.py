from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Conteny-type', 'text/plain')]
    start_response(status, response_headers)
    return [b"Hello World!\n"]

httpserver = make_server('127.0.0.1', 6060, application)
httpserver.handle_request()