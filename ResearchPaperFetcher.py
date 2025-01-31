#For running this script normally please run following commands which installs biopython and Bio python modules
#pip install biopython
#pip install Bio

from Bio import Entrez
import csv
import re

def fetch_pubmed_papers(query, max_results=10, email="pawarsagar1947@gmail.com"):
    Entrez.email = email
  
    try:
        print(f"Searching PubMed for: {query}")
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        search_results = Entrez.read(handle)
        handle.close()

        ids = search_results["IdList"]
        if not ids:
            print("No results found.")
            return []

        papers = []
        for id in ids:
            paper_handle = Entrez.esummary(db="pubmed", id=id)
            summary = Entrez.read(paper_handle)
            paper_handle.close()

            try:
                paper_info = summary[0]

                # Fetch full article details
                details_handle = Entrez.efetch(db="pubmed", id=id, rettype="medline", retmode="text")
                details = details_handle.read()
                details_handle.close()

                # Extract non-academic authors and company names from affiliations
                non_academic_author = extract_non_academic_authors(details)
                company_name = extract_company_names(details)

                # Extract associated email
                associated_email = extract_emails(details)

                papers.append({
                    "PubMedID": id,
                    "Title": paper_info.get("Title", "N/A"),
                    "PubDate": paper_info.get("PubDate", "N/A"),
                    "NonAcademicAuthor": non_academic_author,
                    "CompanyName": company_name,
                    "AssociatedEmail": associated_email
                })
            except (KeyError, IndexError) as e:
                print(f"Error parsing summary for ID {id}: {e}")

        return papers

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def extract_non_academic_authors(details):
    """Extract non-academic authors from affiliations."""
    affiliations = re.findall(r"Affiliation:\s*(.*)", details)
    for aff in affiliations:
        if "Inc." in aff or "LLC" in aff or "Pharma" in aff:
            return aff
    return "N/A"

def extract_company_names(details):
    """Extract company names from affiliations."""
    affiliations = re.findall(r"Affiliation:\s*(.*)", details)
    for aff in affiliations:
        match = re.search(r"(.*(?:Inc\.|LLC|Pharma))", aff)
        if match:
            return match.group(1)
    return "N/A"

def extract_emails(details):
    """Extract email addresses from details."""
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", details)
    return emails[0] if emails else "N/A"

def get_valid_max_results():
    """Prompt the user to enter a valid number for max_results."""
    while True:
        try:
            max_results = int(input("Enter the maximum number of results to fetch: "))
            if max_results > 0:
                return max_results
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_user_email():
    """Prompt the user to enter a valid email address."""
    while True:
        email = input("Enter your email address: ")
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            return email
        else:
            print("Invalid email address. Please try again.")

def save_to_csv(papers, filename="pubmed_papers.csv"):
             try:
                 with open(filename, mode="w", newline="", encoding="utf-8") as file:
                  writer = csv.DictWriter(file, fieldnames=[
                     "PubMedID", "Title", "PubDate", "NonAcademicAuthor", "CompanyName", "AssociatedEmail"
                    ])
                  writer.writeheader()
                  writer.writerows(papers)
                  print(f"Results saved to {filename}")
             except Exception as e:
                print(f"An error occurred while saving to CSV: {e}")

if __name__ == "__main__":
    query = input("Enter your search query: ")
    max_results = get_valid_max_results()
    Entrez.email = get_user_email()

    papers = fetch_pubmed_papers(query, max_results)

    if papers:
        save_to_csv(papers)
    else:
        print("No papers found.")