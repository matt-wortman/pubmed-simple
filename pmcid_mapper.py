#!/usr/bin/env python3
"""
Map PubMed IDs to PubMed Central IDs
Simple. Direct. Clear.

Usage:
    python pmcid_mapper.py pmids.txt
    python pmcid_mapper.py pmids_20240820.txt output.json
"""

import json
import sys
import time
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

def get_pmcids(pmid_list):
    """
    Get PubMed Central IDs for a list of PubMed IDs.
    Uses batch API for efficiency.
    """
    if not pmid_list:
        return []
    
    # NCBI API endpoint
    url = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
    
    # Batch process (API handles up to 200 IDs per request)
    batch_size = 200
    results = []
    
    email = os.getenv('NCBI_EMAIL', 'user@example.com')
    
    for i in range(0, len(pmid_list), batch_size):
        batch = pmid_list[i:i+batch_size]
        
        params = {
            'ids': ','.join(batch),
            'format': 'json',
            'email': email,
            'tool': 'pmcid_mapper'
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            data = response.json()
            
            # Process each record
            for record in data.get('records', []):
                pmid = str(record.get('pmid', record.get('requested-id')))
                pmcid = record.get('pmcid')
                
                results.append({
                    'pubmed_id': pmid,
                    'pmc_id': pmcid if pmcid else None
                })
            
            # Rate limiting
            time.sleep(0.35)  # 3 requests per second
            
        except Exception as e:
            print(f"Error processing batch: {e}")
            # Add nulls for failed batch
            for pmid in batch:
                results.append({
                    'pubmed_id': pmid,
                    'pmc_id': None
                })
    
    return results


def main():
    """Main entry point."""
    
    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage: python pmcid_mapper.py <pmids_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Create output directory structure
    os.makedirs("output/pubmed_centralID", exist_ok=True)
    
    # Set output file path
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = sys.argv[2] if len(sys.argv) > 2 else f"output/pubmed_centralID/pmcid_map_{timestamp}.json"
    
    # Read PMIDs
    print(f"Reading PMIDs from {input_file}...")
    try:
        with open(input_file, 'r') as f:
            pmids = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
        sys.exit(1)
    
    print(f"Found {len(pmids)} PMIDs to process")
    
    # Get PMCIDs
    print("Fetching PubMed Central IDs...")
    mappings = get_pmcids(pmids)
    
    # Count successes
    found = sum(1 for m in mappings if m['pmc_id'])
    print(f"Found {found} PMC IDs out of {len(mappings)} PMIDs")
    
    # Save as clear JSON
    output = {
        'metadata': {
            'total_pmids': len(mappings),
            'pmcids_found': found,
            'pmcids_missing': len(mappings) - found,
            'created': datetime.now().isoformat(),
            'source_file': input_file
        },
        'mappings': mappings
    }
    
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n✅ Results saved to {output_file}")
    print(f"   • Total PMIDs: {len(mappings)}")
    print(f"   • With PMC IDs: {found}")
    print(f"   • Without PMC IDs: {len(mappings) - found}")


if __name__ == "__main__":
    main()