# Test_API Exam

## Description

This project is a simple API test automation using Python, pytest, and Allure report. 

## Sample Result

### Allure HTML Report Home Page
<img src="https://github.com/leonelcalderontest/test_api/blob/main/screenshot_home_page_result_1.PNG" alt="HTML Homepage">



### Allure HTML Report Test Case
<img src="https://github.com/leonelcalderontest/test_api/blob/main/screenshot_test_suite_overview_result_2.PNG" alt="Test Suite -> Test Case 1 Overview">



### Allure HTML Report Sample Logger
<img src="https://github.com/leonelcalderontest/test_api/blob/main/screenshot_test_body_result_3.PNG" alt="Sample Logs on HTML Report">



### Allure HTML Report Sample STDOUT
<img src="https://github.com/leonelcalderontest/test_api/blob/main/screenshot_test_suite_overview_result_4.PNG">

## Requirements

- pytest==7.1.3
- requests~=2.28.1
- allure-pytest==2.11.1
- allure-python-commons==2.11.1

## IDE
- Pycharm
## Python Version
- Python 3.9.0

### Pytest Installation

- pip install pytest

## Running Tests

### Running Tests through PyCharm IDE

1. Open the project in PyCharm.
2. Open the test file `test_api.py`.
3. Right-click inside the test file and select `Run 'pytest in test_api'`.

### Running Tests using Command Prompt (Simple HTML Report)

1. Open the command prompt.
2. Navigate to the project directory.
3. Run the following command:

Note: Need to install pytest-html using the command 
- pip install pytest-html

Before running
- pytest ./test/test_api.py --html=report.html

Check the result in the project folder with a file name of "report.html"

### Running Tests using Command Prompt (Allure HTML Report)

### Allure Command Line Installation

For Windows:
1. Download the latest version of Allure command line tool from the official website: https://github.com/allure-framework/allure2/releases/latest
2. Extract the downloaded ZIP file to a location on your computer (e.g. C:\Program Files\allure)
3. Open a command prompt window.
4. Run the following command to add the Allure executable to the PATH environment variable:
- setx PATH "%PATH%;C:\Program Files\allure\bin"
This command will append the path to the Allure executable to the existing PATH environment variable.
5. Close and reopen the command prompt window to ensure that the changes take effect.
6. Run the allure command to confirm that it is now recognized by the command prompt.

For Mac:

- brew install allure

For Linux:

- sudo apt-add-repository ppa:qameta/allure
- sudo apt-get update
- sudo apt-get install allure

or

- curl -o allure-2.15.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.15.0/allure-2.15.0.tgz &&
- tar -zxvf allure-2.15.0.tgz -C /opt/ &&
- ln -s /opt/allure-2.15.0/bin/allure /usr/bin/allure





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


