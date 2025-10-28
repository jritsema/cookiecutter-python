# cookiecutter-python

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a new Python app.

Scaffolds out a new minimal python project with everything setup and ready to code.


## Usage

### uv

```sh
uvx cookiecutter https://github.com/jritsema/cookiecutter-python.git
```

### pip

```sh
pip install cookiecutter
cookiecutter https://github.com/jritsema/cookiecutter-python.git
```

## Features

- Scaffolds out a new directory with a new Git repo
- Sets up a Python virtual environment
- If you enable [direnv](https://direnv.net/) (optional), it will setup automatic activation of the virtual directory when you `cd` into it and deactivate when you leave
- If you enable [asdf](https://asdf-vm.com/) (optional) it will create a `.tool-versions` file with `direnv` and `python` so that you can run `asdf install` to install required tools.
- Container support: Adds a `Dockerfile` and `.dockerignore`
- If you include AWS SDK, it will add it to your `requirements.txt`
- Includes a `make install` command for installing dependencies and outputting a `piplock.txt` with exact versions, that can be used for reproducible builds
- `make start` will run `main.py` with envvars loaded from `.env` (optional) and enable unbuffered binary I/O


## Example

```
$ cookiecutter https://github.com/jritsema/cookiecutter-python.git
  [1/7] Friendly name of your project (Python app):
  [2/7] Description of your project (This is a new python app):
  [3/7] Directory/URL friendly project name (python-app):
  [4/7] Do you use asdf? [y/n] (y):
  [5/7] Do you use direnv? [y/n] (y):
  [6/7] Do you want to add container support? [y/n] (y):
  [7/7] Do you want to include the AWS SDK? [y/n] (n):
direnv allow .
Creating virtual python environment...
Initialized empty Git repository in /Users/john/code/python-app/.git/
[main (root-commit) 36dde21] Initial commit
 10 files changed, 103 insertions(+)
 create mode 100644 .dockerignore
 create mode 100644 .envrc
 create mode 100644 .gitignore
 create mode 100644 .tool-versions
 create mode 100644 Dockerfile
 create mode 100644 Makefile
 create mode 100644 README.md
 create mode 100644 log.py
 create mode 100644 main.py
 create mode 100644 requirements.txt
Done
cd python-app
```


## TODO

- try to add dynamic python version as cookiecutter variable to be used in Dockerfile
- `container_support` should add a `make build` command
