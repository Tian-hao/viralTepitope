import os
import glob

infiles = sorted(glob.glob('epitope_MHV/*.fasta'))
for infile in infiles:
  inhandle = open(infile)
  lc = 0
  for line in inhandle:
    lc += 1
  inhandle.close()
  if lc == 0: continue
  outfile = infile.replace('.fasta','.blast')
  os.system('blastp -query '+infile+' -db uniprot_ref/uniprot -out '+outfile+' -outfmt 6')
