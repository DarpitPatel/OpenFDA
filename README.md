# OpenFDA
Python code to Scrape data from OpenFDA

The code is used to scrape data from OpenFDA site using its API. Outputs a text file and CSV file with the variables of interest.
Lookup the OpenFDA site for JSON structure to pull other attributes from JSON.

Scraper iterates through results since the maximum records in single API call is restricted to 100

Usage: scraper.py [medicine_name] [iterations]

medicine_name = Name of medicine to pull records

iterations = Desired number of records/100 (May be subjected to API limitation)


