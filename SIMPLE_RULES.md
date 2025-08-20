# The Simple Rules
## Quick Reference for Avoiding Overengineering

### The Prime Directive
**Start simple. Stay simple. Add complexity only when forced by reality.**

---

## 10 Rules to Live By

1. **One File First** - Don't split until you must
2. **Functions Before Classes** - Objects only when needed  
3. **Hard-Code Until It Hurts** - Configure only the third time
4. **Delete Aggressively** - If it's not used now, delete it
5. **Direct Over Clever** - Obvious code is good code
6. **Manual Before Automatic** - Automate only proven workflows
7. **Today's Problem Only** - Don't solve tomorrow's maybe
8. **Explain in 10 Minutes** - Or it's too complex
9. **Three Before Abstract** - No patterns without repetition
10. **Measure Results, Not Architecture** - Speed and size matter

---

## Quick Checks

**Before coding:** "What's the stupidest simple thing that could work?"

**While coding:** "Am I solving a real problem or showing off?"

**After coding:** "What can I delete and still have it work?"

---

## Code Smells

- 📛 Interface with one implementation
- 📛 Factory for simple objects
- 📛 Abstract base class with one child
- 📛 Configuration file with one user
- 📛 Cache for daily-changing data
- 📛 Progress bar for 1-second operation
- 📛 Interactive menu for cron job
- 📛 Multiple files under 100 lines each

---

## The 150-Line Challenge

**Can you solve it in 150 lines or less?**

We replaced 3,490 lines with 150. Most problems are simpler than you think.

---

*Print this. Pin it up. Read it before starting any new project.*