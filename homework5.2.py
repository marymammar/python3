filename = '../dated_file.csv'
fname = '../sorted_file.csv'

def line_by_date(thisline):
    lines = thisline.split()
    date = lines[0]
    return date

fh = open(filename)
readlines = fh.readlines()

# before converting to lambda
#slines = sorted(readlines, key = line_by_date, reverse = True)

# convert to lambda
slines = sorted(readlines, key = lambda thisline: thisline.split()[0],  reverse = True)
wfh = open(fname, 'w', newline='')

for line in slines:
    wfh.write(line)
wfh.close()

print(f'wrote to {fname}')
