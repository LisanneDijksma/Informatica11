from Bio import Entrez
from Bio import SeqIO

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
        #print(record)
        print("bezig")
        gene_dict[gene] = record["IdList"]
    #print(gene_dict)
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
            seq_dict[v] = seq_record.seq
    print(fasta_file)
    return seq_dict

def write_file(gene_dict):
    outfile = open( 'sequences.txt', 'w' )
    for key, value in sorted( gene_dict.items()):
        outfile.write( str(key) + '\t' + str(value) + '\n' )



def main():
    gene_list=read_file()
    gene_dict=find_ID(gene_list)
    seq_dict=find_seq(gene_dict)
    write_file(gene_dict)

main()
