 import json
  2    
  3    filename = '../weny_dod_tiny.json'
  4    
  5    def by_mean_temp(arg):
  6    
  7        print(f'arg to sort function: {arg}')
  8        return int(arg[1]['mean_temp'])
  9    
 10    fh = open(filename)
 11    dod = json.load(fh)
 12    
 13    sorted_dicts = sorted(dod.items(), key= by_mean_temp)
 14    
 15    for key, value in sorted_dicts:
           print(f'{key} : {value}')
