# python-code-kata
Repository for Code Katas based on @pragdave's http://codekata.com/


# Setup

1. If you don't already have a virtualenv installed (or a virtual environment process), setup it up with help from the [Python Packaging User Guide](https://packaging.python.org/en/latest/installing.html#virtual-environments).  In short, for Python <3.4, securely download [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) and then execute the following (omit sudo if you can):

'''
sudo python get-pip.py
sudo pip install -U setuptools
sudo pip install virtualenv
'''

2. Now setup a virtual environment for this repository.

'''
cd python-code-kata
virtualenv .
source bin/activate
'''

3. (Optional) Install any additional libraries.  Pytest is pretty awesome.

'''
pip install -r requirements.txt
'''


# Test Solutions

Place code to solve the Kata in kata_code.py and run test_kata.py with built-in unittest or pytest if installed in step 3.

'''
cd 00_kata_template
python test_kata.py
'''
or
'''
cd 00_kata_template
py.test test_kata.py
'''

Rinse, repeat.  See you at the user group!


# References

[Python Packaging User Guide](https://packaging.python.org/en/latest/installing.html#virtual-environments)
[pytest: Good Integration Practices](http://pytest.org/latest/goodpractises.html#goodpractises)
[Python Guide: Testing Your Code](http://docs.python-guide.org/en/latest/writing/tests/)
[Python Testing: pytest Introduction](http://pythontesting.net/framework/pytest/pytest-introduction/)
