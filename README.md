# simple-crawler
 
This project is a web crawller that works to specific set of URLs, which can consulted at https://github.com/mlpbraga/simple-crawler/blob/main/target-urls.txt.

## Dependencies
    - [Python 3.6 >](https://www.python.org/downloads/)
    - pip3

## Initial Setup
    Install all lib dependencies using `pip3 install -r requirements.txt`

## Usage 
Choose one of the URLs to retrieve data (they can be consulted at https://github.com/mlpbraga/simple-crawler/blob/main/target-urls.txt) and execute `python3 crawller.py [-h] [--print] [--save_csv] [--save_json] target`.

You may print the collected data using `--print` option. The `--save_csv` and `--save_json` options allows the execution to save a file containing execution's retrieved data. This file can be found at `/results` after the execution.
