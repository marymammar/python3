
import re

filename = open('../market_discussion.txt')
file= filename.read()

pattern = r'[A-Z]+, [+-]\d+\.\d{2}\%'
matchboth= re.findall(pattern,file)
matchboth.sort()

for match in matchboth:
    print(match)
