# Task: Map PubMed IDs to PubMed Central IDs

## The Simple Plan

### What We Need
Convert PubMed IDs (e.g., "12345678") to PubMed Central IDs (e.g., "PMC123456") and save as JSON.

### The Stupidest Simple Solution That Could Work

```python
def get_pmcid(pmid):
    """Get PubMed Central ID for a PubMed ID"""
    # Call NCBI API
    # Return PMCID or None
    
def main():
    # Read PMIDs from file
    # For each PMID:
    #   - Get PMCID
    #   - Save to JSON
```

**Estimated lines of code: ~50**

### Step-by-Step Implementation Plan

#### Step 1: Research (5 minutes)
- [ ] Find the NCBI API endpoint for PMID→PMCID conversion
- [ ] Test with curl to verify it works
- [ ] Note the response format

#### Step 2: Write One Function (10 minutes)
- [ ] Create `pmcid_mapper.py` (ONE FILE)
- [ ] Write `get_pmcid(pmid)` function
- [ ] Test with one PMID manually

#### Step 3: Add Main Logic (10 minutes)
- [ ] Read PMIDs from input file
- [ ] Call function for each
- [ ] Save results to JSON

#### Step 4: Test & Ship (5 minutes)
- [ ] Test with 10 PMIDs
- [ ] Verify JSON output
- [ ] Done

**Total time: 30 minutes**
**Total files: 1**
**Total functions: 2 (get_pmcid, main)**

### What We're NOT Building

❌ No classes  
❌ No error handling beyond try/except  
❌ No progress bars (unless > 5 seconds)  
❌ No caching (API is fast)  
❌ No configuration files  
❌ No parallel processing  
❌ No database  
❌ No multiple output formats  
❌ No web interface  
❌ No CLI framework  

### The Simplicity Checklist

- [ ] One file? YES
- [ ] Under 100 lines? YES (target: 50)
- [ ] One clear purpose? YES
- [ ] Could a junior dev understand it? YES
- [ ] Using existing pubmed_search.py patterns? YES

### API Research Notes

NCBI Endpoint for ID conversion:
```
https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/
?ids=PMID1,PMID2
&format=json
```

Returns:
```json
{
  "records": [
    {
      "pmid": "12345678",
      "pmcid": "PMC123456"
    }
  ]
}
```

### Expected Usage

```bash
# Input: PMIDs file (one per line)
# Output: pmid_pmcid_map.json

python pmcid_mapper.py pmids.txt

# Creates:
{
  "12345678": "PMC123456",
  "87654321": "PMC654321",
  "11111111": null  // No PMCID exists
}
```

### Success Criteria

✅ Reads PMIDs from file  
✅ Gets PMCIDs from NCBI  
✅ Saves as JSON  
✅ Under 100 lines  
✅ Works  

### Remember

The last "simple" task was 3,490 lines. This one will be 50.

**Start coding when timer hits 0:00**

---

## Implementation Notes (Fill in as you code)

Started: ___________  
First working version: ___________  
Final line count: ___________  
Actual time taken: ___________  

### What Worked

- 

### What Didn't

- 

### Final Thoughts

- 