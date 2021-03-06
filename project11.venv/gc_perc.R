
#!/usr/bin/Rscript


library('seqinr')
dir.create("Plots")

winsize = 50

genome = read.fasta("nc_sequences.txt")

for (sequence in genome) {
  
  starts = seq(1, length(sequence) - winsize, by = winsize)
  n = length(starts)
  chunkGCs = numeric(n)
  
  for (i in 1:n) {
    chunk = sequence[starts[i]:(starts[i]+winsize)]
    chunkGC = GC(chunk)
    chunkGCs[i] = chunkGC
  }
  pdf(file = paste('Plots/plot-', attr(sequence, 'name'), '.pdf', sep = ''))
  plot(starts, chunkGCs, type='b')
  dev.off()
  print(paste(attr(sequence, 'name'), ' done'))
}

