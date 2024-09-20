# test-to-sdte-lumu-wfc
This repo is the test to show my capabilities about test automation to lumu. Specific the creation of an algorithm to below operations:

- The number of words
- The number of characters
- Key words density section

For that, The project is made up of python to be a cli application.

## Environment
 - Python 3.10

 ## Run tests
To run tests you must follow the next steps:
1. Clone and enter in the repository
~~~
git clone https://github.com/fabian-martinez/test-to-sdte-lumu.git

cd test-to-sdte-lumu-wfc
~~~
2. Configure environment
~~~
python3 -m venv .venv
source .venv/bin/activate
~~~
3. Install dependecies
~~~
pip install -r requirements.txt
~~~
4. Run cli application
~~~
python app --help
~~~

## CLI Options
Use the cli app with below command
~~~
python app [COMMAND] [INPUT] --format=[Default: json / plain / histogram]
~~~
### COMMAND
* file: get text from a .txt file, INPUT: file path
* file: get text from string, INPUT: a string
### format
#### json
~~~
{"words": 6, "characters": 25, "kwd_density": [["one", 3], ["two", 2], ["three", 1]]}
~~~
#### plain
~~~
6 words
25 characters

one: 3
two: 2
~~~
#### histogram
~~~
6 words
25 characters

one    [3]  ****************************************
two    [2]  ***************************
three  [1]  **************
~~~