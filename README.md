# PubMed Paper Fetcher

A Python tool to search and fetch research papers from PubMed based on user-defined queries. This program extracts key details like titles, publication dates, affiliations, company names, and associated emails, and saves the results in a CSV file for further analysis.

## Features

- Search for research papers on PubMed using custom queries.
- Extract:
  - Title
  - Publication Date
  - Non-academic author details
  - Company names
  - Associated email addresses
- Save the fetched data to a CSV file.
- Validates user inputs for a seamless experience.
- Includes detailed comments for easy understanding.


## Prerequisites

- Python 3.7 or later
- [Biopython](https://biopython.org/) library (`pip install biopython`)


## Install required dependencies:
  pip install biopython

## Usages
  Enter your search query, maximum number of results to fetch, and your email address when prompted.

  The program validates inputs and fetches details from PubMed.

  The results are saved in a CSV file (pubmed_papers.csv) in the project directory.

  Input Validation
  Ensures a valid email format.
  Accepts only numeric input for the maximum number of results. Prompts user for correction if the input is invalid.
    Example: 
        Enter your search query: "type 2 diabetes" AND 2020:2024[DP]
        Enter the maximum number of results to fetch: 10
        Enter your email address: example@gmail.com
  Output:
        A CSV file with details of research papers fetched from PubMed.

## Contributing
  Contributions are welcome! Please feel free to fork the repository and submit a pull request.

## Acknowledgments
  PubMed for providing the data.
  Biopython for enabling access to PubMed.

## Feel free to customize it further to match your preferences!
