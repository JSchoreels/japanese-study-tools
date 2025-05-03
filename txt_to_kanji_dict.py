from collections import defaultdict

histogram = defaultdict(int)

for char in txt:
    if (
        char not in {' ', '\n', '[', ']'}
        and not ('\u3040' <= char <= '\u30FF')  # Hiragana & Katakana
    ):
        histogram[char] += 1

# Sort by frequency descending
sorted_histogram = sorted(histogram.items(), key=lambda item: item[1], reverse=True)

# Print in "Kanji: Occurrence" format
for char, count in sorted_histogram:
    print(f"{char}: {count}")

