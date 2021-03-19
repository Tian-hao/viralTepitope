from Bio import SeqIO

infile = open('MHV.pep')
outfile = open('MHV_rename.pep','w')
inhandle = SeqIO.parse(infile,'fasta')
for record in inhandle:
  record.id = record.description.rsplit('[protein_id=')[-1].rsplit(']')[0]
  record.description = ''
  outfile.write(record.format('fasta'))
infile.close()
outfile.close()
