import sys

infile = sys.argv[1]
outfile = infile.replace('.csv','.fasta')
inhandle = open(infile)
outhandle = open(outfile,'w')
header = inhandle.readline()
header = inhandle.readline()
for line in inhandle:
  line = line.rstrip().rsplit(',')
  name = line[0].strip('"')+'_'+line[9].strip('"')+'_'+line[13].strip('"')
  name = name.replace(' ','_')
  seq = line[2].rsplit('+')[0].strip('"')
  if ':' in seq: continue
  outhandle.write('>'+name+'\n'+seq+'\n')
inhandle.close()
outhandle.close()
