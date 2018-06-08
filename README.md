# Informatica11
Workflow project

Auteurs:
Valerie van der Vorst en Lisanne Dijksma.

Beschrijving:
Deze workflow kan met de RNA-Seq input een rapport genereren met informatie over deze genen. 

Er wordt gebruik gemaakt van snakemake om alle scripts achter elkaar uit te voeren. 


Requirements
Systeem

    snakemake 5.1.4
    Linux operating system. De workflow is ontwikkeld in Linux Ubuntu 16.04. 

Dependencies

    
    Miniconda - python3 versie
    R 3.4.4
        library "seqinr"

Preparations

De benodigde bestanden kunnen van github worden gedownload. De map "project11.venv" bevat alle bestanden die nodig zijn voor het uitvoeren van het script. 

Usage

Om het script kan gestart worden in de commandline door via het "cd" commando naar de gedownloade map "project11.venv" te gaan. Hierna kan het "snakemake" commando worden gegeven en wordt de workflow automatisch uitgevoerd. De aangemaakte bestanden worden toegevoegd aan de map en kunnen vanuit daar worden bekeken. 

Output

Na het runnen van de workflow worden er verschillende output bestanden gegegenereerd die worden verwerkt in een rapport. Om dit rapport te bekijken kan er worden geklikt op het .html bestand. 

Belangrijk:

    Als de workflow opnieuw wordt uitgevoerd en er wijzigingen zijn aan de bestanden moeten alle output bestanden worden                
    verwijderd uit de "project11.venv" map, of moet het "snakemake --forceall" commando worden gebruikt. 

