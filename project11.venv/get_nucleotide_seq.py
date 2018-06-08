from Bio import Entrez
from Bio import SeqIO

def read_file():
    file= open("ID.csv", "r")
    gene_list=[]
    file.readline()
    for line in file:
        gene_list.append(line.rstrip('\n').replace('"', ''))
    
    return gene_list

def find_ID(gene_list):
    gene_dict={}
    Entrez.email = "mail@example.org"
    for gene in gene_list:
        handle = Entrez.esearch(db="gene", retmax=10, term=gene, idtype="acc")
        record = Entrez.read(handle)
        gene_dict[gene] = record["IdList"]
    handle.close()  

    return gene_dict  

def find_seq(gene_dict):
    seq=[]
    output_handle = open("nc_sequences.fasta", "w")
    Entrez.email = "mail@example.org"
    for k in gene_dict.keys():
        for v in gene_dict.get(k):
            handle = Entrez.efetch(db="gene", id=v, rettype="text", retmode="text" )
            record = handle.read()
            record_split=record.split("\n")[4]
            id_seq=record_split.split()[1]
            start=record_split.split()[2].split("..")[0].replace("(", "")
            stop=record_split.split()[2].split("..")[1].replace(")", "")


            handle = Entrez.efetch(db="nuccore", id=id_seq, rettype="fasta", retmode="text", seq_start=start, seq_stop=stop)
            record=handle.read()
            seq_record=record.replace(record.split('\n', 1)[0],">"+k)
            seq.append(seq_record)
            print("Ophalen records...")
    
    return seq

def write_file(seq):
    outfile = open( 'nc_sequences.txt', 'w' )
    for sequence in seq:
        outfile.write(sequence)

def main():
    gene_list=read_file()
    gene_dict=find_ID(gene_list)
    seq=find_seq(gene_dict)
    write_file(seq)



main()