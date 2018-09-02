# import http.server
#
#
# class RequestHandler(http.server.SimpleHTTPRequestHandler):
#
#     """
#     HTTP request handler
#     """
#     def do_GET(self):
#
#         try:
#
#             """
#             Resolve and response
#             """
#
#             # body = Message("bucket name", "content")
#
#             print(self.request)
#
#             self.send_response(200)
#             self.send_header('Content-type', 'application/json')
#             self.end_headers()
#             self.wfile.write(self.request)
#
#
#             # do something
#
#             # print(self.path)
#
#         except IOError:
#
#             self.send_error(404, 'Unable to process your request')
#
import syslog
import http.server
import socketserver


PORT = 3333


class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        request_path = self.path

        print("\n----- [DEBUG] jlopez.mx | Request Start ----->\n")
        print("Request path:", request_path)
        print("Request headers:", self.headers)
        print("<----- Request End ----->\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "resolver=jlopez.mx")
        self.end_headers()

	# return None

    def do_POST(self):

        request_path = self.path

        print("\n----- [DEBUG] jlopez.mx | Request Start ----->\n")
        print("Request path:", request_path)

        request_headers = self.headers
        content_length = request_headers.get('Content-Length')
        length = int(content_length) if content_length else 0

        print("Content Length:", length)
        print("Request headers:", request_headers)
        print("Request payload:", self.rfile.read(length))
        print("<----- Request End ----->\n")

        self.send_header('Content-type', 'application/json')
        self.send_response(200)
        self.end_headers()
		
        # return None
    
    do_PUT = do_POST
    do_DELETE = do_GET

    # return None

requestHandler = RequestHandler


httpd = socketserver.TCPServer(("0.0.0.0", PORT), requestHandler) # as httpd:
print("serving at port", PORT)
httpd.serve_forever()
#    print("serving at port", PORT)
#    httpd.serve_forever()
