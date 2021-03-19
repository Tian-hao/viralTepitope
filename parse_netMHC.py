import sys
import glob

infiles = sorted(glob.glob('MHVresult/*.mhc'))
for infile in infiles:
  outfile = infile+'.tsv'
  hla = infile.rsplit('/')[-1].rsplit('_')[0]
  inhandle = open(infile)
  outhandle = open(outfile,'w')
  _ingroup = 0
  for line in inhandle:
    if '<= SB' not in line and '<= WB' not in line: continue
    line = line.rstrip().rsplit()
    if len(line) <= 2: continue
    outhandle.write('\t'.join(line)+'\n')
    #if line[1] == 'HLA-'+hla and _ingroup == 0: 
    #  _ingroup = 1
    #  outhandle.write('\t'.join(line)+'\n')
    #elif line[1] != 'HLA-'+hla and _ingroup == 1:
    #  _ingroup = 0
  inhandle.close()
  outhandle.close()
