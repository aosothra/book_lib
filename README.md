# book_lib - Grandpa's library

This repository contains static files and rendered HTML pages to host a book library for Maxim's grandpa.

You may also find a utility script, that can render a new set of pages based on downloaded library files.

## Installation guidelines

You must have Python3 installed on your system.
You may use `pip` (or `pip3` to avoid conflict with Python2) to install dependencies.

```
pip install -r requirements.txt
```

It is strongly advised to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation.

In order to generate pages and serve book data, you first must acquire said book data. To be specific, you'll need:

- `library.json` library register file.
- `books` directory, containing all book texts, addressed in library register.
- `images` directory, containing all book cover images, addressed in library register.

You can collect all that data in one fell swoop, using [book_snatcher](https://github.com/aosothra/book_snatcher) toolset.

Make sure that your `library.json` file is located next to `render_website.py` script file, and `books`/`images` folders are located in accordance with path schema from `library.json`.

## Basic usage

To render and preview new pages use command:

```
python render_website.py
```

This will render pages and start an HTTP server on [127.0.0.1:5000](http://127.0.0.1:5000/pages/index1.html).

You can stop this server by `KeyboardInterrupt` - `Ctrl+C`

## Project goals

This project was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.