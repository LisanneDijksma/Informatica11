#Inlezen van het bestand
data = read.delim("../Blok11/data/RNA-Seq-counts.txt", header = TRUE, sep = "\t", comment.char = "#")

gene_ID = data[,1]
subset = gene_ID[1:480]

write.csv(subset, file="groot_ID.csv", row.names = F)