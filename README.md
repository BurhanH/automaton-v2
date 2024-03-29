# Automaton-v2
Automation testing framework (UI) - an example. Based on Python, Selenium, and Unittest

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v2/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d13a059853a54c64a33cd307b937996e)](https://app.codacy.com/app/BurhanH/automaton-v2?utm_source=github.com&utm_medium=referral&utm_content=BurhanH/automaton-v2&utm_campaign=Badge_Grade_Dashboard)
[![Python Selenium unittest testing](https://github.com/BurhanH/automaton-v2/actions/workflows/python-app.yml/badge.svg)](https://github.com/BurhanH/automaton-v2/actions/workflows/python-app.yml)


## Requirements
Python 3.6.\*\/3.7.\*\/3.8.\*, Selenium 3.141.0, Unittest, <br>
virtualenv (virtual environment manager), <br> 
Firefox 90.0, geckodriver 0.29.1, <br>
Chrome 81.0.4044.122, chromedriver 81.0.4044.69 <br>

## Project structure
```text
-- automaton-v2
   |-- .gitattributes
   |-- .gitignore
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   `-- tests
       |-- browser.py
       |-- initial.py
```

## How to prepare environment
1) Install [Python](https://www.python.org/downloads/)
2) Install and configure [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3) Clone or copy (download) the repository into your virtual environment
4) Activate virtual environment, move to `automaton-v2` folder, and execute command `pip install -r requirements.txt`
5) Install Firefox / Chrome web browser
6) Download, extract and move geckodriver / chromedriver into `bin` folder for Mac/Linux, `Scripts` folder for Windows on virtual environment

## How to run tests
1) Open terminal window
2) Move to virtual environment folder
3) Activate virtual environment
4) Move to `automaton-v2` folder
5) Execute `python -m unittest discover tests "*.py" -v`

## How to run test/s in Chrome browser
Go to any UI scenario and change the value of the `BROWSER` variable from `firefox` to `chrome`. <br> Note! Before execution read steps 5-6 from [How to prepare environment](https://github.com/BurhanH/automaton-v2#how-to-prepare-environment) section

## Technology stack and helpful info
[Python 3.6](https://docs.python.org/3.6/) / [Python 3.7](https://docs.python.org/3.7/) / [Python 3.8](https://docs.python.org/3.8/)<br>
[virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) <br>
[GitHub, cloning repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) <br>
[unittest](https://docs.python.org/3.7/library/unittest.html) <br>
[Selenium](https://www.selenium.dev/documentation/en/) <br>
[Firefox](https://www.mozilla.org/en-US/firefox/) <br>
[geckodriver](https://github.com/mozilla/geckodriver/releases) <br>
[Chrome](https://www.google.com/chrome/) <br>
[ChromeDriver](https://chromedriver.chromium.org/downloads) <br>
