from http.server import HTTPServer, SimpleHTTPRequestHandler


def main():
    try:
        server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
        print(f'Serving on {server.server_address[0]}:{server.server_address[1]}')
        server.serve_forever()        
    except KeyboardInterrupt:
        print('Shutting server down...')
        server.shutdown()

if __name__=="__main__":
    main()