# AKDM-Anagram-Solver
An anagram solver to ease us in

## Description
A Python-based anagram solver that can identify valid words and present alternative anagram words. This program uses Python's standard library for efficient anagram detection.

## Features
- Validates whether input words are valid
- Finds all anagrams of a given word from a word list
- Uses efficient dictionary-based lookup for fast anagram matching
- Interactive command-line interface
- Support for custom word lists

## Requirements
- Python 3.6 or higher
- No external dependencies (uses Python standard library only)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Dillon742/AKDM-Anagram-Solver.git
   cd AKDM-Anagram-Solver
   ```

2. (Optional) Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Note: Currently no external dependencies are needed.

## Usage

### Basic Usage (Default Word List)
Run the anagram solver with a built-in default word list:
```bash
python3 anagram_solver.py
```

### Using a Custom Word List
You can provide your own word list file (one word per line):
```bash
python3 anagram_solver.py words.txt
```

### Example Session
```
$ python3 anagram_solver.py
============================================================
AKDM Anagram Solver
============================================================

Using default word list with 44 words

Enter words to find anagrams (or 'quit' to exit)
------------------------------------------------------------

Enter a word: listen

'listen' is a valid word

Found 4 anagram(s):
  - enlist
  - inlets
  - silent
  - tinsel

Enter a word: quit

Thank you for using AKDM Anagram Solver!
```

## How It Works
1. **Word Validation**: The program checks if the input word exists in the loaded word list
2. **Anagram Detection**: Uses a sorted character key approach - all anagrams of a word have the same sorted letters
3. **Efficient Lookup**: Pre-processes the word list into a dictionary for O(1) anagram lookups

## Word List
The repository includes a sample `words.txt` file with common English words. You can replace or extend this with your own word list.

## License
See LICENSE file for details.
