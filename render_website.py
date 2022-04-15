import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked

def render_page():
    pages_dir = 'pages'

    with open('library.json', 'r', encoding='utf-8') as lib_file:
        lib_register = json.loads(lib_file.read())

    env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html'])
        )
    index_template = env.get_template('index-template.html')

    os.makedirs(pages_dir, exist_ok=True)
    for num_page, books_on_page in enumerate(chunked(lib_register, 20)):
        rendered_book_page = index_template.render(
            num_page=num_page,
            book_pairs=chunked(books_on_page, 2)
        )
        page_fullpath = os.path.join(pages_dir, f'index{num_page}.html')
        with open(page_fullpath, 'w', encoding='utf-8') as html_file:
            html_file.write(rendered_book_page)


def main():
    render_page()

    server = Server()
    server.watch('templates/*.html', render_page)
    server.serve(host='localhost', port=5000)

if __name__=="__main__":
    main()