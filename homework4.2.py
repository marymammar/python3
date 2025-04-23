

import re

file= '../access_log.txt'
filename = open(file)
bytes_dict = {}
for line in filename:
    matchid = re.search(r'~([a-zA-z]+\d+)',line)
    matchbytes = re.search(r'(\d+)$',line)

    if not matchid or not matchbytes:
        continue
    stuid = matchid.group(1)
    bytes = int(matchbytes.group(1))

    if stuid not in bytes_dict:
        bytes_dict[stuid]= 0
    bytes_dict[stuid] = bytes_dict[stuid] + bytes

filename.close()

for key in sorted(bytes_dict, key=bytes_dict.get, reverse= True):
    if bytes_dict[key] > 10000000:
        print(f'{key}:  {bytes_dict[key]}')
