# The below script will find the matches only the beginning of the file means it will find first words
import re
text = "Python for Devops automation"
pattern = r"Python"
result = re.match(pattern,text)
print(result)