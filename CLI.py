import argparse
from ResearchPaperFetcher import fetch_pubmed_papers
import re
import csv

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")

    # Positional argument: Query
    parser.add_argument("query", help="Search query for PubMed articles")

    # Optional arguments
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results")
    parser.add_argument("-e", "--email", type=validate_email, default="pawarsagar1947@gmail.com",help="email for NCBI")
    parser.add_argument("-n", "--num", type=int, default=10, help="Number of results to fetch (default: 10).")

    # Parse arguments from the command line
    args = parser.parse_args()

    # Debug Mode
    if args.debug:
        print("[DEBUG] Arguments received:", args)

    # Fetch PubMed articles
    articles = fetch_pubmed_papers(args.query, args.num, args.email)

    # Output results
    if args.file:
            try:
                with open("pubmed_research_papers", mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=[
                         "PubMedID", "Title", "PubDate", "NonAcademicAuthor", "CompanyName", "AssociatedEmail"
                    ])
                    writer.writeheader()
                    writer.writerows(articles)
                    print("Results saved to pubmed_research_papers")
            except Exception as e:
                print(f"An error occurred while saving to CSV: {e}")

    else:
        print("Fetched Articles:\n", articles)

def validate_email(email):
    """Validate email address format."""
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise argparse.ArgumentTypeError("Invalid email address format")
    return email

if __name__ == "__main__":
    main()
