import json
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, Template, select_autoescape

def main():
    with open('library.json', 'r', encoding='utf-8') as lib_file:
        lib_register = json.loads(lib_file.read())

    env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html'])
        )
    index_template = env.get_template('index-template.html')
    rendered_index_page = index_template.render(
        books=lib_register
    )

    with open('index.html', 'w', encoding='utf-8') as html_file:
        html_file.write(rendered_index_page)

    try:
        server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
        print(f'Serving on {server.server_address[0]}:{server.server_address[1]}')
        server.serve_forever()        
    except KeyboardInterrupt:
        print('Shutting server down...')
        server.shutdown()

if __name__=="__main__":
    main()