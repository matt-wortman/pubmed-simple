# The Simplicity Guidelines
## Hard-Won Rules for Avoiding Overengineering

*These guidelines were extracted from replacing a 3,490-line system with 150 lines that work better.*

---

## Core Principle

> **Start with the simplest solution that could possibly work. Only add complexity when reality proves it necessary.**

---

## The Rules

### 1. Start With a Single File
- **BEGIN** with one script file
- **ONLY** split into multiple files when the single file exceeds 500 lines
- **RESIST** the urge to "organize" prematurely

### 2. No Abstractions Until You Have Three
- **WAIT** until you have three concrete implementations
- **THEN** consider abstracting the common pattern
- **NEVER** create an interface with one implementation

### 3. Functions Over Classes
- **START** with functions
- **USE** classes only when you need to maintain state between calls
- **AVOID** classes that only have an `__init__` and one other method

### 4. Hard-Code First, Configure Later
- **BEGIN** with hard-coded values
- **EXTRACT** to configuration only after you've needed to change it twice
- **RESIST** making everything configurable "just in case"

### 5. YAGNI (You Aren't Gonna Need It)
- **DELETE** any code not currently being used
- **REMOVE** "might need later" features
- **TRUST** version control to remember deleted code

### 6. The 10-Minute Rule
- **IF** you can't explain what your code does in 10 minutes
- **THEN** it's too complex
- **SIMPLIFY** until a junior developer can understand it quickly

### 7. Manual Before Automatic
- **DO** it manually first
- **AUTOMATE** only after you've done it manually at least three times
- **MEASURE** if automation actually saves time

### 8. Direct Over Indirect
- **PREFER** `requests.get()` over `APIClient.make_request()`
- **CHOOSE** obvious over clever
- **VALUE** readability over flexibility

### 9. The One-Week Test
- **ASK**: "If I leave for a week, can someone else run this?"
- **IF** they need more than a README, it's too complex
- **SIMPLIFY** until the answer is yes

### 10. Measure What Matters
- **COUNT** lines of code (fewer is better)
- **TIME** execution (faster is better)
- **TRACK** dependencies (fewer is better)
- **IGNORE** architectural "purity"

---

## Red Flags to Avoid

### 🚩 Architecture Astronomy
- Multiple layers of abstraction
- Interfaces with single implementations
- Factory patterns for simple objects
- Dependency injection for static dependencies

### 🚩 Premature Optimization
- Caching data that changes frequently
- Async/parallel processing for sub-second operations
- Database for hundreds of items
- Microservices for single-user tools

### 🚩 Feature Creep
- Interactive menus for batch jobs
- Progress bars for operations under 5 seconds
- Configurable everything
- Multiple ways to do the same thing

### 🚩 Test Theater
- More test code than production code
- Testing configuration instead of logic
- Mocking everything
- 100% coverage of trivial code

---

## Questions to Ask Before Coding

### Before Starting:
1. **Can this be a single function?**
2. **Can this be a single file?**
3. **What's the simplest possible solution?**
4. **Am I solving the actual problem or an imagined one?**

### While Coding:
1. **Is this abstraction necessary right now?**
2. **Will someone understand this without explanation?**
3. **Am I adding this because I need it or because I might need it?**
4. **Would a hard-coded solution work for now?**

### Before Committing:
1. **Can I remove any code and still have it work?**
2. **Can I combine any files?**
3. **Can I replace any classes with functions?**
4. **Would my past self understand this immediately?**

---

## The Simplicity Checklist

Before declaring any project "done", verify:

- [ ] **Single file?** Or justified multiple files?
- [ ] **Under 500 lines?** Or justified complexity?
- [ ] **Minimal dependencies?** Only what's essential?
- [ ] **No unused code?** Everything has a purpose?
- [ ] **README sufficient?** No extensive documentation needed?
- [ ] **10-minute explainable?** Clear to newcomers?
- [ ] **Directly testable?** Can run with simple commands?
- [ ] **No premature abstractions?** Concrete implementations?

---

## Real-World Example

### ❌ What Not To Do:
```python
class APIClientFactory:
    def create_client(self, config: Config) -> BaseAPIClient:
        return NCBIAPIClient(config)

class BaseAPIClient(ABC):
    @abstractmethod
    def search(self, query: str) -> SearchResults:
        pass

class NCBIAPIClient(BaseAPIClient):
    def __init__(self, config: Config):
        self.session = SessionManager(config)
        self.cache = CacheManager(config)
        # ... 50 more lines of setup
```

### ✅ What To Do Instead:
```python
def search_pubmed(query, email, api_key):
    response = requests.get(
        'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',
        params={'db': 'pubmed', 'term': query, 'retmode': 'json',
                'email': email, 'api_key': api_key}
    )
    return response.json()['esearchresult']['idlist']
```

---

## The Ultimate Test

**Can you delete 50% of your code and still solve the problem?**

If yes, you're not done simplifying.

---

## Remember

> "It seems that perfection is attained not when there is nothing more to add, but when there is nothing more to remove."  
> — Antoine de Saint-Exupéry

Your code should be a tool, not a monument to your engineering skills.

**Simple code is not unprofessional. Overengineered code is.**

---

## Enforcement

1. **Code reviews** should ask: "Can this be simpler?"
2. **Sprint planning** should ask: "What's the minimal solution?"
3. **Architecture discussions** should start with: "Do we need architecture?"
4. **Retrospectives** should measure: "Did we overengineer anything?"

---

## Final Word

The 3,490-line system we replaced didn't start that way. It grew through a thousand small decisions to add "just one more abstraction" or "make it a bit more flexible."

**Complexity is entropy. It grows naturally. Simplicity requires constant vigilance.**

Stay simple. Stay vigilant.