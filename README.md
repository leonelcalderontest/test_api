# Test_API Exam

## Description

This project is a simple API test automation using Python, pytest, and Allure report. 

## Requirements

- Python 3.9
- Pytest
- Allure Command Line

### Pytest Installation

- pip install pytest

### Allure Command Line Installation

- For Windows:
- scoop install allure

- or

- choco install allure.commandline

- For Mac:

- brew install allure

- For Linux:

- sudo apt-add-repository ppa:qameta/allure
- sudo apt-get update
- sudo apt-get install allure

- or

- curl -o allure-2.15.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.15.0/allure-2.15.0.tgz &&
- tar -zxvf allure-2.15.0.tgz -C /opt/ &&
- ln -s /opt/allure-2.15.0/bin/allure /usr/bin/allure


## Running Tests

### Running Tests through PyCharm IDE

1. Open the project in PyCharm.
2. Open the test file `test_api.py`.
3. Right-click inside the test file and select `Run 'pytest in test_api'`.

### Running Tests through Command Prompt

1. Open the command prompt.
2. Navigate to the project directory.
3. Run the following command:

- pytest ./test/test_api.py --html=report.html

### Running Tests with Allure Report through Command Prompt

1. Open the command prompt.
2. Navigate to the project directory.
3. Run the following commands:

- allure serve allure-results --clean --silent
- pytest ./test/test_api.py --alluredir=allure-results
- allure generate allure-results -o html_allure_local_result --clean
- allure report open -o html_allure_local_result

## Author

Leonel Calderon

## Contributing


## License


