# python-example

# Install

With asdf:
- add plugin in .tool-version "asdf add plugin xx"
- install plugin "asdf install"
- export PATH="~/.asdf/shims:$PATH"

With python:
- install venv "python -m venv venv"
- active venv "source venv/bin/activate"
- install dep with poetry "poetry install"
- create requirements "poetry export -f requirements.txt --output requirements.txt"
