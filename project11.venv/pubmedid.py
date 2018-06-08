# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:06:47 2018

@author: xx_xx
"""
from Bio import Entrez
import csv

def read_file():
    file= open("groot_ID.csv", "r")
    gene_list=[]
    file.readline()
    for line in file:
        gene_list.append(line.rstrip("\n"))
    return gene_list

def find_ids(gene_list):
    Entrez.email = "mail@mail.com"
    id_list = []
    count=0
    for single_term in gene_list:
        count+=1
        data = Entrez.esearch(db="pubmed",term = single_term)
        res = Entrez.read(data)
        pmids = res["IdList"]
        print("Zoeken...", count, "van 480")
        print(pmids)
        if not pmids ==[]:
            found = [single_term]
            for i in pmids:
                found.append(i)
            id_list.append(found)
    return id_list

def sort_list(id_list):
    id_list.sort(key=len)
    return id_list

def savelist(a):
    with open("pubmedids.csv", 'w') as outcsv:  
         wr = csv.writer(outcsv)
         wr.writerows(a)
         
def main():
    genes = read_file()
    id_list = find_ids(genes)
    sortedlist = sort_list(id_list)
    savelist(sortedlist)
main()
