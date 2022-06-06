from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def sayHello():
	return 'Hello World From XMLRPCServer '

server = SimpleXMLRPCServer(("localhost",8000))
print("server sudah siap")
server.register_function(sayHello,"sayHello")
server.serve_forever()