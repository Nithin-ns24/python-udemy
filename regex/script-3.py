# this will find all pattern searches in how many places are there more then 1 time
import re
text = "python for automating devops tasks using python"
pattern = r"python"
result = re.findall(pattern,text)
print(result)