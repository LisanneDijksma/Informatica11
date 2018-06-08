# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:16:31 2018

@author: xx_xx
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 21:59:49 2018

@author: xx_xx
"""

from Bio import Entrez
from Bio import SeqIO
import csv

def read_file():
    file= open("ID.csv", "r")
    gene_list=[]
    file.readline()
    for line in file:
        gene_list.append(line.rstrip('\n'))
    
    return gene_list

def find_ID(gene_list):
    gene_dict={}
    Entrez.email = "mail@example.org"
    for gene in gene_list:
        handle = Entrez.esearch(db="Protein", retmax=10, term=gene, idtype="acc")
        record = Entrez.read(handle)
        gene_dict[gene] = record["IdList"]
    handle.close()  

    return gene_dict

def find_seq(gene_dict):
    seq_dict={}
    count=0
    Entrez.email = "mail@example.org"
    output_handle = open("sequences.fasta", "w")
    for k in gene_dict.keys():
        for v in gene_dict.get(k):
            handle = Entrez.efetch(db="Protein", id=v, rettype="fasta", retmode="text" )
            seq_record = SeqIO.read(handle, 'fasta')
            print(seq_record)
            fasta_file=SeqIO.write(seq_record, output_handle, "fasta")
            print("in bestand")
            sequence = seq_record.description
            if k in seq_dict:
                    l = seq_dict.get(k)
                    #print(k)
                    m = []
                    if isinstance(l, list):
                        for n in l: 
                            m.append(n)
                    else:
                        m.append(l)
                    if sequence not in m:
                        m.append(sequence)
                    seq_dict.update({k:m})
                #voegt j als een nieuwe key toe aan de dictionary    
            else:
                seq_dict[k] = []
                seq_dict.update({k:sequence})
            
    print(fasta_file)
    return seq_dict  
def savelist(a, bestandnaam):
    with open(bestandnaam, 'w', newline='') as outcsv:  
        wr = csv.writer(outcsv)
        wr.writerow(["sample_id","function"])
        wr.writerows(a.items())
def main():
    gene_list=read_file()
    gene_dict=find_ID(gene_list)
    seq_dict=find_seq(gene_dict)
    savelist(seq_dict, "functions_per_id.csv")

main()
