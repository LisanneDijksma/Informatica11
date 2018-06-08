# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:06:47 2018

@author: xx_xx
"""
from Bio import Entrez
import csv

#leest bestand in dat in dezelfde directory staat als het script
def read_file():
    file= open("ID.csv", "r")
    gene_list=[]
    file.readline()
    for line in file:
        gene_list.append(line.rstrip("\n"))
        #print(line)
    return gene_list
#find pubmed ids bij de sample ids
def find_ids(gene_list):
    Entrez.email = "mail@mail.com"
    id_list = []
    for single_term in gene_list:
        data = Entrez.esearch(db="pubmed",term = single_term)
        res = Entrez.read(data)
        pmids = res["IdList"]
        if not pmids ==[]:
            found = [single_term]
            for i in pmids:
                found.append(i)
            id_list.append(found)
    print(id_list)
    print("lol")
    return id_list
#sorteert de lijst op aantal pubmed ids per sample(van minder naar meer)
def sort_list(id_list):
    id_list.sort(key=len, reverse=True)
    print(id_list)
    return id_list
#slaat lijst op als csv in dezelfde directory als het script
def savelist(a):
    with open("pubmedids.csv", 'w', newline = '') as outcsv:  
         wr = csv.writer(outcsv)
         wr.writerow(["sample_id","articles on pubmed"])
         wr.writerows(a)
         
def main():
    genes = read_file()
    id_list = find_ids(genes)
    sortedlist = sort_list(id_list)
    savelist(sortedlist)
main()