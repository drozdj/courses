Use good tools[¶](#use-good-tools "Permalink to this headline")
===============================================================

Use the tools introduced in each section[¶](#use-the-tools-introduced-in-each-section "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------

For your convenience, here is a list of tools and packages discussed in each section of the book.

### Set up your project[¶](#set-up-your-project "Permalink to this headline")

[git](https://git-scm.com/)

a command line tool for code versioning

[github](https://github.com/)

a website where you can share code

[conda](https://docs.conda.io/en/latest/)

a command line package manager and virtual environment manager

[setuptools](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html)

a Python library to define pip installable packages

[cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.3/)

a command line tool to create projects from templates

--- 

### Keep things tidy[¶](#keep-things-tidy "Permalink to this headline")

[flake8](https://flake8.pycqa.org/en/latest/) and [pylint](https://pylint.org/)

command line linters for Python

[black](https://github.com/psf/black)

a command line auto-formatter for Python code, with plugins for popular IDEs

[vulture](https://github.com/jendrikseipp/vulture)

a Python package to identify dead code in your codebase

[jupytext](https://github.com/mwouts/jupytext)

a command line tool to seamlessly translate between regular jupyter notebooks and a markdown-based representation

---

### Write decoupled code[¶](#write-decoupled-code "Permalink to this headline")

[pandas](https://pandas.pydata.org/)

a Python library to represent columnar data

[xarray](http://xarray.pydata.org/en/stable/)

a Python library to represent multidimensional tensors with named dimensions

[collections](https://docs.python.org/3/library/collections.html)

a Python standard library of containers, including defaultdict, counter, etc.

---

### Test your code[¶](#test-your-code "Permalink to this headline")

[pytest](https://docs.pytest.org/en/6.2.x/)

a Python library for unit testing, along with a command line utilities

---

### Write good docs[¶](#write-good-docs "Permalink to this headline")

[argparse](https://docs.python.org/3/library/argparse.html)

a Python library to parse command-line arguments, part of the Python standard library

[shellcheck](https://github.com/koalaman/shellcheck)

a command-line tool that checks for common errors in bash scripts, with plugins for popular IDEs

[make](https://www.gnu.org/software/make/)

a command-line tool to define and run directed acyclic graphs of computation

[sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)

a command-line tool to generate documentation from Python code and text files

[readthedocs](https://readthedocs.org/)

a website to host documentation

---

### Make it social[¶](#make-it-social "Permalink to this headline")

[vscode live share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)

IDE extension for code sharing

[deepnote](https://deepnote.com/) and [cocalc](https://cocalc.com/)

collaborative jupyter notebooks in the browser

[replit](https://replit.com)

collaborative IDE in the browser

Choose an IDE[¶](#choose-an-ide "Permalink to this headline")
-------------------------------------------------------------

Integrated development environments (IDE) can help you develop faster and make it easy to implement some of the productivity tips I’ve discussed previously. Preferred IDEs change from year to year, as new editors become favored while others are shunned. Don’t be surprised if in three years you’ll be using a different IDE.


[I’ve evaluated many IDEs](https://xcorr.net/2013/04/17/evaluating-ides-for-scientific-python/), and overall, I like [vscode](https://code.visualstudio.com/) best. It’s open source, free, and fast. It has very good integrated Python development tools, and it has an impressive array of plugins for almost any imaginable use case. The git and github tools are particularly well integrated, which makes it easy to do source control outside of the command line. There is an integrated debugger, as well as a terminal, so it’s one-stop shop for development.

Others recommend [PyCharm](https://www.jetbrains.com/pycharm/) - it has best-in-class code understanding, and scales well to large codebases. It’s free for academics.

Use WSL on Windows[¶](#use-wsl-on-windows "Permalink to this headline")
-----------------------------------------------------------------------

Windows’ basic terminal lacks basic features. Powershell is powerful but it is very different from other platforms. For a while, the best way to get a Unix-style shell on Windows was to use the git bash tool. In my opinion, these days the best-in-class terminal to use on Windows is _Windows subsystem for Linux_ (WSL).

_WSL_ is an emulation layer that allows you to run a full Linux kernel inside of a Windows terminal window. [Once installed](https://docs.microsoft.com/en-us/windows/wsl/install-win10), you can install any Linux OS you like - Ubuntu being the _de facto_ standard.

You won’t be able to run GUI applications. However, many tools you’ll want to use run webservers, for example jupyter - you’ll be able to access these through your your normal Windows-based web browser, such as Chrome, Firefox or Edge. Your Linux installation will run in a virtual filesystem, which you can access through Windows explorer by typing `explorer` inside a WSL terminal. `code .` will fire up a version of vscode in your current directory.

Acknowledgements
© Copyright 2021–2022.  
Licensed under [CC-BY 4.0](https://github.com/patrickmineault/codebook/blob/main/LICENSE) \[[source](https://github.com/patrickmineault/codebook)\].  
[Report issue](https://github.com/patrickmineault/codebook/issues).
