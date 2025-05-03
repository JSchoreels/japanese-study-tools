#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Regular expressions for character types
hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'
kanji = r'[㐀-䶵一-鿋豈-頻]'
radicals = r'[⺀-⿕]'
katakana_half_width = r'[｟-ﾟ]'
alphanum_full = r'[！-～]'
symbols_punct = r'[、-〿]'
misc_symbols = r'[ㇰ-ㇿ㈠-㉃㊀-㋾㌀-㍿]'
ascii_char = r'[ -~]'

# Get file path from first CLI argument
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Read text from file
with open(filename, 'r', encoding='utf-8') as f:
    txt = f.read()

# Build histogram
histogram = defaultdict(int)

# Filter characters based on given patterns (exclude kana, symbols, etc.)
for char in txt:
    # Check if character matches any of the specified categories
    if re.match(kanji, char):
        histogram[char] += 1

# Sort and print
for char, count in sorted(histogram.items(), key=lambda item: item[1], reverse=True):
    print(f"{char}: {count}")