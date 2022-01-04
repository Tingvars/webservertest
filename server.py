import http.server
import socketserver
import json

counter = 0

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global counter
        f = open('viewcounter.json')
        data = json.load(f)
        for i in data["counter"]:
            counter = int(i)
        f.close()
        counter+= 1
        printstring = '{"counter": [' + str(counter) + '] }'
        with open("viewcounter.json", mode="w") as file:
            file.write(str(printstring))
        # http.server.SimpleHTTPRequestHandler.do_GET(self)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"<div>{counter}</div>".encode())

PORT = 8080
Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving the website at port # ", PORT)
    httpd.serve_forever()