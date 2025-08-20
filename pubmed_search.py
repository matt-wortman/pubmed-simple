#!/usr/bin/env python3
"""
PubMed Search for Cincinnati Children's Hospital
Simple. Fast. Effective.

Usage:
    python pubmed_search.py                      # All time
    python pubmed_search.py 2024/01/01           # From date to now  
    python pubmed_search.py 2024/01/01 2024/12/31  # Date range
"""

import json
import os
import sys
import time
from datetime import datetime
import requests
from dotenv import load_dotenv

# Load configuration
load_dotenv()

def search_pubmed(from_date=None, to_date=None):
    """
    Search PubMed for Cincinnati Children's papers.
    
    Args:
        from_date: Start date (YYYY/MM/DD format)
        to_date: End date (YYYY/MM/DD format)
        
    Returns:
        List of PubMed IDs
    """
    # Get credentials
    email = os.getenv('NCBI_EMAIL')
    api_key = os.getenv('NCBI_API_KEY')
    
    if not email or not api_key:
        print("Error: Missing NCBI credentials")
        print("Please set NCBI_EMAIL and NCBI_API_KEY in .env file")
        sys.exit(1)
    
    # Load institution variations
    try:
        with open('approved_variations.json', 'r') as f:
            variations = json.load(f)['variations']
    except FileNotFoundError:
        print("Error: approved_variations.json not found")
        sys.exit(1)
    
    # Build affiliation query
    affiliations = ' OR '.join([f'"{v}"[Affiliation]' for v in variations])
    query = f"({affiliations})"
    
    # Add date range if specified
    if from_date:
        date_range = f"{from_date}:{to_date or '3000/12/31'}[dp]"
        query = f"{query} AND {date_range}"
    
    # Search parameters
    params = {
        'db': 'pubmed',
        'term': query,
        'retmax': 100000,  # Try higher limit
        'retmode': 'json',
        'email': email,
        'api_key': api_key
    }
    
    # Execute search
    print(f"Searching PubMed for Cincinnati Children's papers...")
    if from_date:
        print(f"Date range: {from_date} to {to_date or 'current'}")
    
    try:
        response = requests.get(
            'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',
            params=params,
            timeout=30
        )
        response.raise_for_status()
        
        # Parse results
        data = response.json()
        pmids = data['esearchresult']['idlist']
        total = int(data['esearchresult']['count'])
        
        if total > len(pmids):
            print(f"Note: Found {total} papers total, returned first {len(pmids)}")
            print(f"      (NCBI limit per request is 10,000)")
        
        return pmids
        
    except requests.RequestException as e:
        print(f"Error connecting to PubMed: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error parsing PubMed response: {e}")
        sys.exit(1)


def save_results(pmids, from_date=None, to_date=None):
    """Save search results to organized output directory."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Add year to filename if searching a specific year range
    year_suffix = ""
    if from_date and to_date:
        from_year = from_date.split('/')[0]
        to_year = to_date.split('/')[0]
        if from_year == to_year:
            year_suffix = f"_{from_year}"
    
    # Create output directory structure
    os.makedirs("output/pubmedID", exist_ok=True)
    
    # Save PMIDs
    pmid_file = f"output/pubmedID/pmids_{timestamp}{year_suffix}.txt"
    with open(pmid_file, 'w') as f:
        for pmid in pmids:
            f.write(f"{pmid}\n")
    
    # Save summary in main output directory
    summary_file = f"output/search_summary_{timestamp}{year_suffix}.txt"
    with open(summary_file, 'w') as f:
        f.write(f"Cincinnati Children's PubMed Search Results\n")
        f.write(f"{'='*50}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Papers found: {len(pmids):,}\n")
        if from_date:
            f.write(f"Date range: {from_date} to {to_date or 'current'}\n")
        f.write(f"Output file: {pmid_file}\n")
    
    print(f"\n✅ Found {len(pmids):,} papers")
    print(f"📄 PMIDs saved to: {pmid_file}")
    print(f"📊 Summary saved to: {summary_file}")


def main():
    """Main entry point."""
    # Parse command line arguments
    from_date = sys.argv[1] if len(sys.argv) > 1 else None
    to_date = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Search
    pmids = search_pubmed(from_date, to_date)
    
    # Save results
    if pmids:
        save_results(pmids, from_date, to_date)
    else:
        print("No papers found")


if __name__ == "__main__":
    main()