
  1    from datetime import datetime
  2    
  3    filename = '../dated_file.csv'
  4    fname = '../sorted_file.csv'
  5    
  6    
  7    def line_by_date(thisline):
  8        lines = thisline.split()
  9        date = lines[0]
 10        return date
 11    
 12    fh = open(filename)
 13    readlines = fh.readlines()
 14    fh.close()
 15    # before converting to lambda
 16    #slines = sorted(rreadlineseadlines, key = line_by_date, reverse = True)
 17    
 18    # convert to lambda
 19    slines = sorted(readlines, key = lambda thisline: datetime.strptime(thisline.split(',')[0], '%m/%d/%Y'))
 20    wfh = open(fname, 'w', newline='')
 21    
 22    for line in slines:
 23        wfh.write(line)
 24    wfh.close()
 25    
 26    print(f'wrote to {fname}')
