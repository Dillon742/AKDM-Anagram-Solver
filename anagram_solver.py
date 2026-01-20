#!/usr/bin/env python3
"""
AKDM Anagram Solver
A Python program to solve anagrams by identifying valid words and presenting alternatives.
"""

import sys
from collections import defaultdict


class AnagramSolver:
    """Main class for solving anagrams."""
    
    def __init__(self, word_list_file=None):
        """
        Initialize the anagram solver with a word list.
        
        Args:
            word_list_file: Path to a file containing valid words (one per line).
                          If None, uses a default word list.
        """
        self.words = set()
        self.anagram_dict = defaultdict(list)
        
        if word_list_file:
            self.load_word_list(word_list_file)
        else:
            self.load_default_words()
    
    def load_word_list(self, filename):
        """
        Load words from a file.
        
        Args:
            filename: Path to the word list file.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    word = line.strip().lower()
                    if word and word.isalpha():
                        self.words.add(word)
                        # Store words by their sorted letters for quick anagram lookup
                        key = ''.join(sorted(word))
                        self.anagram_dict[key].append(word)
            print(f"Loaded {len(self.words)} words from {filename}")
        except FileNotFoundError:
            print(f"Error: Word list file '{filename}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading word list: {e}")
            sys.exit(1)
    
    def load_default_words(self):
        """Load a small default set of words for demonstration."""
        default_words = [
            'listen', 'silent', 'enlist', 'inlets', 'tinsel',
            'heart', 'rate', 'tear', 'tare', 'earth', 'hater',
            'stop', 'post', 'spot', 'tops', 'pots', 'opts',
            'evil', 'vile', 'live', 'veil',
            'angel', 'angle', 'glean',
            'canoe', 'ocean',
            'crate', 'trace', 'react', 'cater',
            'care', 'race', 'acre',
            'table', 'bleat',
            'stone', 'notes', 'tones', 'onset',
            'pear', 'reap', 'rape', 'pare',
            'are', 'era', 'ear',
        ]
        
        for word in default_words:
            self.words.add(word)
            key = ''.join(sorted(word))
            self.anagram_dict[key].append(word)
        
        print(f"Using default word list with {len(self.words)} words")
    
    def is_valid_word(self, word):
        """
        Check if a word is valid (exists in the word list).
        
        Args:
            word: The word to check.
        
        Returns:
            bool: True if the word is valid, False otherwise.
        """
        return word.lower() in self.words
    
    def find_anagrams(self, input_word):
        """
        Find all anagrams of the input word from the word list.
        
        Args:
            input_word: The word to find anagrams for.
        
        Returns:
            list: A list of anagram words (excluding the input word itself).
        """
        input_word = input_word.lower()
        key = ''.join(sorted(input_word))
        
        # Get all words with the same sorted letters
        anagrams = self.anagram_dict.get(key, [])
        
        # Remove the input word from results (if it exists)
        result = [word for word in anagrams if word != input_word]
        
        return result
    
    def solve(self, input_word):
        """
        Main method to solve anagrams.
        
        Args:
            input_word: The word to solve anagrams for.
        
        Returns:
            dict: A dictionary with 'valid' (bool), 'anagrams' (list), and 'message' (str).
        """
        input_word = input_word.strip()
        
        if not input_word:
            return {
                'valid': False,
                'anagrams': [],
                'message': 'Error: Empty input'
            }
        
        if not input_word.isalpha():
            return {
                'valid': False,
                'anagrams': [],
                'message': 'Error: Input must contain only letters'
            }
        
        is_valid = self.is_valid_word(input_word)
        anagrams = self.find_anagrams(input_word)
        
        return {
            'valid': is_valid,
            'anagrams': anagrams,
            'message': f"'{input_word}' is {'a valid' if is_valid else 'not a valid'} word"
        }


def main():
    """Main function to run the anagram solver CLI."""
    print("=" * 60)
    print("AKDM Anagram Solver")
    print("=" * 60)
    print()
    
    # Check if a custom word list file was provided
    word_list_file = None
    if len(sys.argv) > 1:
        word_list_file = sys.argv[1]
    
    # Initialize the solver
    solver = AnagramSolver(word_list_file)
    print()
    
    # Interactive mode
    print("Enter words to find anagrams (or 'quit' to exit)")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\nEnter a word: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using AKDM Anagram Solver!")
                break
            
            if not user_input:
                continue
            
            result = solver.solve(user_input)
            
            print()
            print(result['message'])
            
            if result['anagrams']:
                print(f"\nFound {len(result['anagrams'])} anagram(s):")
                for anagram in sorted(result['anagrams']):
                    print(f"  - {anagram}")
            else:
                print("\nNo anagrams found in the word list.")
        
        except KeyboardInterrupt:
            print("\n\nThank you for using AKDM Anagram Solver!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
