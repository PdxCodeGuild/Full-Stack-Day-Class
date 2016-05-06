# Python Packages and Dependencies
Thus far you have been giving the Python interpreter already installed on your computer single Python source files to run.

Real Python programs are more complex than single files.
But you know how to make [your own modules](modules.md) and could imagine making a complex program.

Sometimes, you've imported modules from the standard library.
You haven't needed to install anything.
The whole point of the standard library is that those modules are always there in every Python installation.

People have made thousands of Python **packages** that contain other modules you can use.
This is great!
Folks have done your work for you.
When you use these other packages, they are **dependencies**.

But, these packages aren't provided by default with every Python interpreter.
Conveniently, Python comes with a package manager [Pip](pip.md) that makes installing most packages very easy.

If you want to give your code to someone else to run, you need some way of telling them about all of the packages you need.
And not only that!
You have to ensure they have a compatible _version_ and that all of the dependencies of your dependencies are installed.
That is done via a [requirements file](py-app-requirements.md).

The other person who's running your code also might need to deal with having multiple applications to run!
What if they all had different requirements?

The first step to solving these problems is knowing how to create _isolated_ sets of installed packages.
Then you can explicitly know what dependencies you've installed, what versions you have, and not worry about anyone else's application.
This is done through [virtualenvs](virtualenv.md).
