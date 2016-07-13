# Python

The programming language we'll be learning in this course is [Python](https://www.python.org).

It is an interpreted language.
You save your source in a `.py` file and a special program called the **interpreter** knows how to run that file.

## Install

### OS X

First, install [Homebrew](http://brew.sh).
It's a package manager that allows you to install other command line tools very easily.
We'll use it a few times later in the class as well.

Then, install Python 3 and setup the Python command.

```bash
brew install python3
echo "alias python='python3'" >> ~/.bashrc
echo "alias python2='\python'" >> ~/.bashrc
echo "alias pip='pip3'" >> ~/.bashrc
echo "alias pip2='\pip'" >> ~/.bashrc
cat <<EOF >> ~/.profile
if [[ \$- == *i* ]]; then
    [[ "\$SHELL" == *bash && -r ~/.bashrc ]] && source ~/.bashrc
fi
EOF
alias python='python3'
alias python2='\python'
alias pip='pip3'
alias pip2='\pip'
```

### Windows 7 and 10

![](py.images/0000.png)
[Download](https://www.python.org/downloads/) the Python 3 installer and run it.

![](py.images/0001.png)
If you are not sure then please ask which executable you should download. Most people will be needing `x86-64 executable installer` because they have 64-bit processors and admin priveleges on their machine.

![](py.images/0002.png)
![](py.images/0003.png)
Be sure to select, **Add Python 3.5 to PATH**

![](py.images/0004.png)
![](py.images/0005.png)

![](py.images/0006.png)
To verify your install, please launch powershell.

![](py.images/0007.png)
![](py.images/0008.png)

![](py.images/0009.png)
**pip** is the python package manager. This will become increasingly important later. To update **pip** please run `pip install --upgrade pip`

![](py.images/0012.png)
**ipython** is a very helpful python-shell that i will sugest use for understanding code.

## Running

Once you've installed Python, you should be able to run Python source files.

```bash
~ $ python -V
Python 3.5.1
```

Also check that you can run PIP.

```bash
~ $ pip -V
pip 8.1.2 from /usr/local/lib/python3.5/site-packages (python 3.5)
```
