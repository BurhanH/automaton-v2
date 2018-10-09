# automaton-v2
Automation framework (UI) - an example. Based on Python, Selenium, and Unittest

[![Build Status](https://travis-ci.org/BurhanH/automaton-v2.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v2)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d13a059853a54c64a33cd307b937996e)](https://app.codacy.com/app/BurhanH/automaton-v2?utm_source=github.com&utm_medium=referral&utm_content=BurhanH/automaton-v2&utm_campaign=Badge_Grade_Dashboard)

# Quick start!

#### Requirements
Python 3.6.\*, Selenium 3.14.0, Unittest, virtualenv (virtual environment manager), 
Firefox 62.\*, geckodriver 0.22, Chrome 69.*, chromedriver 2.42

#### How to prepare environment
1) Install Python - https://www.python.org/downloads/
2) Install and configure virtualenv - https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
3) Clone or copy (download) the repository into your virtual environment
4) Activate virtual environment, move to `automaton-v2` folder, and execute command `pip install -r requirements.txt`
5) Install Firefox / Chrome web browser
6) Download, extract and move geckodriver / chromedriver into `bin` folder for Mac/Linux, `Scripts` folder for Windows on virtual environment

#### How to run tests
1) Open terminal window
2) Move to virtual environment folder
3) Activate virtual environment 
4) Move to `automaton-v2` folder
5) Execute `python -m unittest discover tests "*.py" -v`

To be continue ...