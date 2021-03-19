import os
import glob

infiles = sorted(glob.glob('MHV_rename.pep'))
reffile = open('HLA_list.txt')
for line in reffile:
  hla = 'HLA-'+line.rstrip().replace('*','').replace(':','')
  for infile in infiles:
    outfile = 'MHVresult/'+hla+'_'+infile.replace('_rename.pep','.mhc')
    print(outfile)
    os.system('~/Tools/netMHC/netMHC-4.0/netMHC '+infile+' -a '+hla+' -s 1> '+outfile)
reffile.close()
reflist = ['H-2-Kd','H-2-Kb','H-2-Dd','H-2-Db']
for hla in reflist:
  for infile in infiles:
    outfile = 'MHVresult/'+hla+'_'+infile.replace('_rename.pep','.mhc')
    print(outfile)
    os.system('~/Tools/netMHC/netMHC-4.0/netMHC '+infile+' -a '+hla+' -s 1> '+outfile)

