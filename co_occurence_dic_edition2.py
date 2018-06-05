# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:16:54 2018

@author: xx_xx
"""

from Bio import Entrez
import csv
from collections import defaultdict
from collections import OrderedDict

#leest bestand in dat in dezelfde directory staat als het script
def read_file():
    file= open("pubmedids.csv", "r")
    gene_list=[]
    for line in file:
        gene_list.append(line.rstrip("\n"))
        #print(line)
    gene_list = list(filter(len, gene_list))
    #print(gene_list)
    return gene_list

def find_article(genes):
    Entrez.email = "Your.Name.Here@example.org"
    allarticles={}
    for pubmedid in genes:
        pmid =pubmedid.split(",")
        ids = pmid[0].replace('"', '')
        #print(ids)
        alllinks = []
        for i in pmid[1:]:
            handle = Entrez.elink(dbfrom="pubmed", id=i, linkname="pubmed_pubmed")
            record = Entrez.read(handle)
            handle.close()
            #print(record[0]["LinkSetDb"][0]["LinkName"])
            linked = [link["Id"] for link in record[0]["LinkSetDb"][0]["Link"]]
            #print(linked)
            alllinks.append(linked)
            for i in alllinks:
                for j in i:
                    #checkt of j als een k in de dictionary staat, maakt een lijst van alle values van de key wanneer dit zo is en updat de key met de ljst+ nieuwe gen id)
                    if j in allarticles:
                       k = allarticles.get(j)
                       #print(k)
                       m = []
                       if isinstance(k, list):
                           for l in k:
                               m.append(l)
                       else:
                           m.append(k)
                       if ids not in m:
                           m.append(ids)
                       allarticles.update({j:m})
                   #voegt j als een nieuwe key toe aan de dictionary    
                    else:
                        allarticles[j] = []
                        allarticles.update({j:ids})

    print(allarticles)
    return allarticles


def sortdictionary(d):
    #verwijdert artikelen waar maar 1 sample in voorkomt.
    entitiesToRemove = []    
    #voegt de artikelen met maar 1 sample toe aan een lijst
    for key in d:
        if isinstance(d.get(key), list) == False:
            entitiesToRemove.append(key)
        elif len(d.get(key)) == 1:
            entitiesToRemove.append(key)

#verwijdert alle artikelen die voorkomen in de gemaakte lijst uit de dictionary
    for x in entitiesToRemove:
        if x in d:
            d.pop(x)

    #sorteert de dictionary met artikelen op het aantal samples per artikelen van meer naar minder.
    sorteddic = OrderedDict(sorted(d.items(), key=lambda x:len(x[1]), reverse=True))
    return sorteddic

#maakt een csv met een gegeven bestandnaam aan in dezelfde directory als het script
def savelist(a, bestandnaam):
    with open(bestandnaam, 'w', newline='') as outcsv:  
        wr = csv.writer(outcsv)
        wr.writerow(["pubmed articles","sample_id"])
        wr.writerows(a.items())

def main():
    genes = read_file()
    linklist = find_article(genes)
    sorteddic = sortdictionary(linklist)
    savelist(sorteddic, "SamplesInSamePubmedArticle.csv")
   # simlist = similarities(linklist)
    #savelist(simlist, "simlist.csv")
    
    
main()