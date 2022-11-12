#! usr/bin/envs python 


import vcf 
vcf_reader = vcf.Reader(filename='tb.vcf.gz')
vcf_writer = vcf.Writer(open('test.vcf', 'w'), vcf_reader)
for record in vcf_reader:
     vcf_writer.write_record(record)
