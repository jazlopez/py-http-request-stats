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
import datetime 
import socketserver


PORT = 3333
# f = open("mirror.payload.log", "w")

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_LOG(self, length, request_headers, payload):
      f = open("mirror.payload.log", "a+")
      dt = str(datetime.datetime.now())
      log = []
     
      print("<---- [DEBUG] jlopez.mx | Request Start --->")
      log.append("<---- [DEBUG] jlopez.mx | Request Start --->")
      log.append("\n")
      print("Content Length:", length)
      log.append(":".join(["Content Length", str(length)]))
      log.append("\n")
      print("Request headers:", request_headers)
      log.append(":".join(["Request headers", request_headers]))
      log.append("\n")
      payload = str(payload)
      print("Request Payload:", payload)
      log.append(":".join(["Request time", dt]))
      log.append("\n")
      log.append(":".join(["Request payload", payload]))
      log.append("\n")	
      print("<---- REQUEST END ---->")
      log.append("<---- REQUEST END ---->\n")

      f.writelines(log)
      f.close()

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

        # print("\n----- [DEBUG] jlopez.mx | Request Start ----->\n")
        # print("Request path:", request_path)

        request_headers = self.headers
        content_length = request_headers.get("content-length")
        length = int(content_length) if content_length else 0
        payload = self.rfile.read(length)

        # self.do_LOG(length, str(request_headers), payload)
        # print("Content Length:", length)
        # print("Request headers:", request_headers)
        # print("Request payload:", self.rfile.read(length))
        # print("<----- Request End ----->\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "resolver=jlopez.mx")
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.do_LOG(length, str(request_headers), payload)
        return None	
        # return None
    
    do_PUT = do_POST
    do_DELETE = do_GET

    # return None

requestHandler = RequestHandler


httpd = socketserver.TCPServer(("0.0.0.0", PORT), requestHandler) # as httpd:
print("serving at port", PORT)
httpd.serve_forever()
f.close()
#    print("serving at port", PORT)
#    httpd.serve_forever()
