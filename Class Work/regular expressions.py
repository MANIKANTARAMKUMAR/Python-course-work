import re
pattern = r"[0-9]"
res=re.search(pattern,"abc4def")
print("Search Result:",res.group())
print(res.group()if res else "No match found")
matches=re.findall(pattern,"abc4def5ghi6")
print("Findall Matches:",matches)
