import re

def word_frequency(text):
  clean_text = re.sub(r'[^\w\s]', '', text.lower())
  words = clean_text.split()
    
  counts = {}
  for word in words:
    counts[word] = counts.get(word, 0) + 1
    return counts

sample_text = """
JavaScript is a versatile, dynamically typed programming language that brings life to web pages by making them interactive.
It is used for building interactive web applications, supports both client-side and server-side development, and integrates seamlessly with HTML, CSS, and a rich standard library.
"""

freq_dict = word_frequency(sample_text)

top_5 = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:5]

print("--- Top 5 Common Words ---")
for word, count in top_5:
  print(f"{word}: {count}")