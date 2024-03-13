import re

text = "Python is more in-demand than Golang"
pattern = r"Golang"

replacement = "any language"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)