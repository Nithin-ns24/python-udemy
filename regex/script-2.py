# This script will search for patterns where all there
import re
text = "Python for Devops automation"
pattern = r"Devops"
result = re.search(pattern,text)
print(result)