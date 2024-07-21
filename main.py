from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = input("Escribe la IP del servidor: ")
PORT = 8000


class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content/type", "text/hmtl")
        self.end_headers()
        with open("index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        self.wfile.write(bytes(html_content, "utf-8"))
        
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content/type", "aplication/json")
        self.end_headers
        fecha =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "'+fecha+'"}', "utf-8"))


server =HTTPServer((HOST, PORT), NeuralHTTP)
print("Servidor Corriendo")
server.serve_forever()
server.server_close()
print("Servidor Detenido")