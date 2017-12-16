# tsv2nt
Python 3 script to convert all tsv(tab separated values) files in a directory to n-triples files saved in another directory
From each line of the tsv file, certain values are required as subject, predicate and object. You need to change those values and you are good to go.
Converted N-Triples file will be saved in another folder in current working directory named "nt-files"
Save all tsv files in one directory and using command line command, type the following command.
./tsv2nt.py directory-with-tsv-files
for example:  ./tsv2nt.py /tsv_files
