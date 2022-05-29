from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
import cgitb

cgitb.enable()


def interface_exec(file):
    handle = __import__(file)
    return handle.doGET()


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        url = unquote(self.path).split('?')
        if len(url) == 1: url.append('blank_param=0')

        if url[0][-4:] == '.dpy':
            params0 = url[1].split('&')
            finalparams = {}
            for i in params0:
                i2 = i.split('=')
                finalparams[i2[0]] = i2[1]
            msg = __import__(url[0].split('/')[-1].replace(
                '.dpy', '')).doGET(finalparams)
        else:
            msg = 'Access to this URL is forbidden, ' + __import__('dir').doGET({})

        self.wfile.write(bytes(str(msg), 'utf-8'))


with HTTPServer(('', 80), handler) as server:
    print('Server started.')
    server.serve_forever()
