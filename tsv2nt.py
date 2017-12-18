#!/usr/bin/env python3
#./tsv2nt.py directory-with-tsv-files
#./tsv2nt.py /tsv_files

import os,sys
import pathlib


nt_output_folder = os.getcwd() + "/nt-files/"
tsv_files = []

def load_tsv_filenames(directory):
    for path, subdirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".tsv"):
                tsv_files.append(pathlib.PurePath(path, file_name))
            else:
                print("Fatal filename unknown " + file_name)
    return

def filter_file(tsv_file):

    directory = os.path.join(os.getcwd(), nt_output_folder)

    file_link = os.path.join(directory,os.path.basename(tsv_file).strip(".tsv") + '.nt')

    nt_fp = open(file_link, 'w+', encoding="utf-8")
    tsv_fp = open(tsv_file, 'r', encoding="utf-8")
    next(tsv_fp)
    for line in tsv_fp:
        #print(line)
        if len(line.split("\t"))==6:
            triple = "<http://en.wikipedia.org/wiki?curid=" + line.split("\t")[0]  + ">\t<http://lod.openaire.eu/vocab/resOriginalID>\t\""  + line.split("\t")[5].strip("\n") + "\" .\n"
            #print("%s"%(triple))
            nt_fp.write("%s"%(triple))
    nt_fp.close()
    tsv_fp.close()
    return

######################################################################################
if __name__ == "__main__":

    tsv_folder = os.getcwd() + sys.argv[1]
    print (tsv_folder)
    load_tsv_filenames(tsv_folder) #load clusters with links
    if os.path.exists(os.path.join(os.getcwd(),nt_output_folder)) == False:
        os.mkdir(os.path.join(os.getcwd(),nt_output_folder))
    print(tsv_files)
    filter_file(tsv_files[4])
    for file in range(len(tsv_files)):
        break
        print("Now processing file number %s named %s"%(file,tsv_files[file]))
        filter_file(file)
