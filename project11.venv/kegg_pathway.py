# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:06:47 2018

@author: xx_xx
"""
from Bio.KEGG import REST
import csv

def read_file():
    file= open("ID.csv", "r")
    gene_list=[]
    file.readline()
    for line in file:
        gene_list.append(line.rstrip("\n").replace('"', ''))
        print(line)
    return gene_list
def find_kegg(genes):
    count=0
    lpl_pathways = REST.kegg_list("pathway", "lpl").read()
    entries = []
    for line in lpl_pathways.rstrip().split("\n"):
        entry, description = line.split("\t")
        #print(line)
        entries.append(entry)
    print(entries)               
    pathway = {}
    for i in genes:
        for entry in entries:
            count+=1
            get = REST.kegg_get(entry, option=None)
            get_read = get.readlines()
            if any(i in s for s in get_read):
                print(entry)
                print(i)                
            #checkt of j als een k in de dictionary staat, maakt een lijst van alle values van de key wanneer dit zo is en updat de key met de ljst+ nieuwe gen id)
                if i in pathway:
                    k = pathway.get(i)
                    #print(k)
                    m = []
                    if isinstance(k, list):
                        for l in k: 
                            m.append(l)
                    else:
                        m.append(k)
                    if entry not in m:
                        m.append(entry)
                    pathway.update({i:m})
                   #voegt j als een nieuwe key toe aan de dictionary    
                else:
                    pathway[i] = []
                    pathway.update({i:entry})
            print(pathway, count)
    print(pathway)
    return pathway

def savelist(a, bestandnaam):
    with open(bestandnaam, 'w', newline='') as outcsv:  
        wr = csv.writer(outcsv)
        wr.writerow(["sample_id","KEGG pathway id"])
        wr.writerows(a.items())
        
def main():
    genes = read_file()
    dic_pathways = find_kegg(genes)
    savelist(dic_pathways, "allpathways.csv")
    
main()
