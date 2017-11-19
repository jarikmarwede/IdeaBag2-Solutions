# Welcome
This document specifies how to contribute to the repository.

### Table Of Contents
* [Contributing code](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#contributing-code)
  * [Contributing a new project](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#contribute-a-new-project)
  * [Contributing to an existing project](https://github.com/jarik-marwede/IdeaBag2-Projects/blob/master/CONTRIBUTING.md#contribute-to--an-existing-project)

## Contributing code

### Contributing a new project

When adding a new project please remember:
* Add a shebang line
* Add a module docstring
* Add ways to both import the project and to run it individually
* All rules for contributing to existing projects

### Contributing to an existing project

When improving a project please follow these rules:
* Always add docstrings
* Use comments for everything not self explanatory
* Keep the Zen of Python in mind
* Before commiting check your code for codestyle issues

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
In generall, all projects should follow the [PEP 8](https://pep8.org/) styleguide.
However this is just a suggestion.
Just try to make your code as readable as possible.

To automatically check for PEP 8 complience use:
* [Pylint](https://www.pylint.org/)
* [Flake8](https://pypi.python.org/pypi/flake8)
