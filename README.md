## Website

All the sources for my website: [jgrizou.com](jgrizou.com)

### License

You are allowed to reuse the code that builds the website ([GPL3 license](http://www.gnu.org/licenses/gpl.html)) but not the content of the website itself which is under the ```./src``` folder.

### About

I am using:

- [pandoc](http://pandoc.org/) as the main file converter
- [panzer](https://github.com/msprev/panzer) that create style for pandoc, simply more convenient
- [jinja2](http://jinja.pocoo.org/docs/dev/) because pandoc is not that magic and some more advanced templating must be done with jinja, I use mostly filter.
- [python-bibtexparser](https://github.com/sciunto-org/python-bibtexparser) and [citeproc-py](https://github.com/brechtm/citeproc-py)for handling publication to make my publication page
- I did some python tools and the builder scripts, because I prefer knowing what is going on to customize better.

It is very clunky but it works for me. There are some weird things due to the limit of templating in pandoc. It is not documented.
