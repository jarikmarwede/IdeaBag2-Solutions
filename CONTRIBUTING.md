# Welcome
This document specifies how to contribute to the repository.

### Table Of Contents
* [Contributing code](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#contributing-code)
  * [Contributing a new program](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#contributing-a-new-program)
  * [Contributing to an existing program](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#contributing-to-an-existing-program)

## Contributing code

### Contributing a new program

When adding a new program please remember:
* Add a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line
* Add a module docstring containing the title and the description of the idea from *Idea Bag 2*
* Add ways to both import the program and to run it individually
* Try to use only modules from the standard library, if possible
* If the program requires more than one file you should create a folder named after the program in the appropriate category
* All rules for [contributing to existing programs](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#contributing-to-an-existing-program)

### Contributing to an existing program

When improving a program please follow these rules:
* Always add docstrings
* Use comments for everything not self explanatory
* Keep the [Zen of Python](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#the-zen-of-python) in mind
* Before commiting check your code for [codestyle](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#codestyle) issues

#### The Zen of Python
The Zen of Python are some generall suggestions on how to write python code.

You can view it by using 
```python 
import this
```
inside the python shell.

> The Zen of Python, by Tim Peters
>
> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!

#### Codestyle
In generall, all programs should follow the [PEP 8](https://pep8.org/) styleguide.
However this is just a suggestion.
Just try to make your code as readable and understandable as possible.

To automatically check for PEP 8 complience use:
* [Pylint](https://www.pylint.org/)
* [Flake8](https://pypi.python.org/pypi/flake8)
