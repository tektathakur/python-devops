import re

text = "Python is quite in demand"
pattern = r"Python"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

