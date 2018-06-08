#Inlezen van het bestand
data = read.delim("../Blok11/data/RNA-Seq-counts.txt", header = TRUE, sep = "\t", comment.char = "#")

gene_ID = data[,1]
selected = gene_ID[100:120]
print(selected)


write.csv(selected, file="ID.csv", row.names = F)


