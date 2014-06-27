
TEST_FILE_INDEX = range(2,4)
CMD = "go run main.go -g ../test_data/data{0}.fasta -s ../test_data/data{0}.vcf  > /tmp/tmp_out ; diff /tmp/tmp_out ../test_data/data{0}.out"

import os
for i in TEST_FILE_INDEX:
   cmd = CMD.format(i)
   print cmd
   os.system(cmd)

