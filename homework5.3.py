import json

filename = '../weny_lod_tiny.json'

def by_mean_temp(arg):
    print(f'arg to sort function: {arg}')
    return arg['mean_temp']

fh = open(filename)
lod = json.load(fh)

sorted_dicts = sorted(lod, key= by_mean_temp, reverse = True)

for ldict in sorted_dicts:
    print(ldict)
