from server import *


server = Server()
server.start_server()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop_server()