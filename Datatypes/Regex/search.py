import re

text = "Toddler jumped in the mud"
pattern = r"jumped"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")