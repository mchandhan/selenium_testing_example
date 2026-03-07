# Selenium Page Title Tests with HtmlTestRunner

This repository contains simple Selenium tests written in Python using the `unittest` framework.  
The tests open Google and Facebook, print their page titles, and generate an HTML report using [HtmlTestRunner](https://pypi.org/project/html-testRunner/).

## Requirements

- Python 3.8+
- Google Chrome browser
- ChromeDriver (managed automatically via `webdriver-manager`)
- The following Python packages:
  ```bash
  pip install selenium webdriver-manager html-testRunner
  ```
## Project Structur
```
.
├── test.py        # Main test script
├── reports/       # HTML reports generated after test runs
└── README.md      # Project documentation
```
##  Running the Test

```
python test.py
```

This will:
- Launch Chrome in headless mode.
- Navigate to Google and Facebook.
- Print the page titles in the console.
- Generate an HTML report in the reports/ directory.

## Example output

Console:

```
google title: Google
facebook title: Facebook – log in or sign up
..
----------------------------------------------------------------------
Ran 2 tests in 5.123s

OK
```

## HTML Report

An HTML file will be created in the reports/ folder showing test results in a user‑friendly format.

## Customization

- To run Chrome with a visible window, remove the --headless option in Options().
- To skip tests, use the @unittest.skip decorator.
- To add more sites, create additional test methods starting with test_.

