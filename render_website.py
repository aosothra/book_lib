from http.server import HTTPServer, SimpleHTTPRequestHandler


def main():
    server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__=="__main__":
    main()