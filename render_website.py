import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked

def render_page():
    with open('library.json', 'r', encoding='utf-8') as lib_file:
        lib_register = json.loads(lib_file.read())

    env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html'])
        )
    index_template = env.get_template('index-template.html')
    rendered_index_page = index_template.render(
        book_pairs=chunked(lib_register, 2)
    )

    with open('index.html', 'w', encoding='utf-8') as html_file:
        html_file.write(rendered_index_page)


def main():
    render_page()

    server = Server()
    server.watch('templates/*.html', render_page)
    server.serve(host='localhost', port=5000)

if __name__=="__main__":
    main()