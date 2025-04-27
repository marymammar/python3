import json

filename = '../weny_dod_tiny.json'

def by_mean_temp(arg):
    print(f'arg to sort function: {arg}')
    return arg

fh = open(filename)
dod = json.load(fh)

sorted_dicts = sorted(dod, key= by_mean_temp)

for key in sorted_dicts:
    print(f'{key} : {dod[key]}')
