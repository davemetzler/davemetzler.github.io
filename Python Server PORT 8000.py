import os
#os.chdir('C:\Users\Dave Metzler.SUMMIT\Documents\WEBSITE')
import SimpleHTTPServer
import SocketServer

PORT = 8001

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print ("serving at port", PORT)
httpd.serve_forever()
