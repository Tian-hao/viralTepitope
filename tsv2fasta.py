import sys
import glob

infiles = sorted(glob.glob('epitope_MHV/*.tsv'))
for infile in infiles:
  outfile = infile.replace('.tsv','.fasta')
  inhandle = open(infile)
  outhandle = open(outfile,'w')
  header = inhandle.readline()
  for line in inhandle:
    #if ':' in line: continue #discrete epitope
    line = line.rstrip().rsplit('\t')
    name = line[1]+'_'+line[10]
    seq = line[2]
    outhandle.write('>'+name+'\n'+seq+'\n')
  inhandle.close()
  outhandle.close()
