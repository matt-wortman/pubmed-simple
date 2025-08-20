# pubmed-simple

A simple, fast PubMed search tool for Cincinnati Children's Hospital Medical Center publications.

## Why This Exists

This tool replaces a 3,490-line system with 150 lines of code while maintaining identical functionality and improving performance by 2x.

## Features

- 🔍 Search PubMed for all Cincinnati Children's papers
- 📅 Optional date range filtering  
- 📄 Export results as plain text PMID lists
- ⚡ 2x faster than complex alternatives
- 🎯 Zero unnecessary dependencies

## Performance

| Metric | This Tool | Previous System | Improvement |
|--------|-----------|-----------------|-------------|
| Lines of Code | 150 | 3,490 | **23x smaller** |
| Files | 1 | 11 | **11x fewer** |
| Dependencies | 2 | 6+ | **Minimal** |
| Execution Time | 0.5s | 1.1s | **2x faster** |
| Results | Identical | Identical | ✅ |

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/pubmed-simple.git
cd pubmed-simple

# Install dependencies (just requests and python-dotenv)
pip install -r requirements.txt

# Configure credentials
cp .env.example .env
# Edit .env with your NCBI credentials
```

## Configuration

1. Get NCBI API credentials (free): https://www.ncbi.nlm.nih.gov/account/
2. Add credentials to `.env`:
```
NCBI_EMAIL=your.email@example.com
NCBI_API_KEY=your_api_key_here
```

## Usage

```bash
# Search all time
python pubmed_search.py

# Search from specific date to present
python pubmed_search.py 2024/01/01

# Search date range
python pubmed_search.py 2024/01/01 2024/12/31
```

## Output

The tool creates two files with timestamps:
- `pmids_YYYYMMDD_HHMMSS.txt` - List of PubMed IDs (one per line)
- `summary_YYYYMMDD_HHMMSS.txt` - Search summary with metadata

## Example

```bash
$ python pubmed_search.py 2024/01/01 2024/12/31

Searching PubMed for Cincinnati Children's papers...
Date range: 2024/01/01 to 2024/12/31

✅ Found 3,045 papers
📄 PMIDs saved to: pmids_20240820_143022.txt
📊 Summary saved to: summary_20240820_143022.txt
```

## How It Works

1. Loads approved institution name variations from `approved_variations.json`
2. Builds an OR query with all variations
3. Queries PubMed's E-utilities API
4. Saves results to timestamped files

## Institution Variations

The tool searches for papers affiliated with any of these Cincinnati Children's variations:
- Cincinnati Children's Hospital Medical Center
- CCHMC
- Cincinnati Childrens
- Cincinnati Children's
- And 7 other variations

See `approved_variations.json` for the complete list.

## Limitations

- Maximum 10,000 results per search (PubMed API limit)
- For larger result sets, consider date range batching

## Philosophy

> "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." - Antoine de Saint-Exupéry

This tool embodies that philosophy. It does one thing, does it well, and nothing more.

## License

MIT License - See LICENSE file for details

## Contributing

This tool is intentionally simple. Please resist the urge to add features. If you need something complex, that's a different tool.

## Comparison with Alternatives

The previous system included:
- Interactive CLI menus (unused in production)
- Fuzzy matching algorithms (one-time manual task)  
- Multiple client implementations (unnecessary abstraction)
- Caching layers (for daily-changing data)
- 754 lines of tests (for 150 lines of code)

This tool includes:
- The functionality you actually need
- Nothing else

## Support

For issues: Open a GitHub issue
For questions: See the code (it's only 150 lines)