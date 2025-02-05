# Frequency Analyzer

### How to install

```bash
git clone https://github.com/wesfly/frequency-analyzer
cd frequency-analyzer
```
To use this script, simply save it as a Python file (e.g., `frequency_counter.py`) and run it:
```bash
python3 frequency_counter.py
```

This Python script counts the frequency of each letter in a given string and displays the results in a dictionary format. Here's how it works:

1. **Input**: The user is prompted to enter a string of text.
2. **Alphabet Initialization**: A list containing all lowercase English letters (a-z) is defined.
3. **Counting Occurrences**: For each letter in the alphabet, the script counts how many times it appears in the input string and stores these counts in a list.
4. **Results Display**: The script prints the total length of the input string and converts the counts into a dictionary where keys are letters (a-z) and values are their respective counts.

### Features:
- The script handles both lowercase and uppercase letters by default (though it only counts lowercase).
- Non-letter characters are treated as separate entities with their own counts.
- The script does not modify the input string or change case.