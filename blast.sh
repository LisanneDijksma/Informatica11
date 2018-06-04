#!/bin/bash

#Uitvoeren van blastp
blastp -query "sequences.fasta" -db nr -remote -out "blast_results.xml"