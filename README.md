# Phenotype_Genotype_Ataxia

![flow](https://github.com/NCBI-Hackathons/pheno_geno_ataxia/blob/master/genotype-phenotype_tool.png "Logo Title Text 1")

This project is a tool-kit used to analyze the role of multifactorial inheritance  in rare disease. There is currently unaccounted for variation in the severity of rare disease phenotypes, some of which will be explainable by modifier alleles. The goal of this project is to provide a tool-kit that can be used to identify the genes that are modulating disease phenotypes.

The first step to identifying the disease phenotype modulating genes is to reduce the search space. The user can filter the genes based on the likihood that a gene is involved in the phenotye. Currently the residual variation intolerance scores and the polyphen scores may be used to filter genes based on how intolerant the gene is to mutations and the predicted impact of the mutation. The user may also filter the genes based on gene ontology annotation to restrict the search to genes involved in particular pathways or functions. 

After filtering the user can use the apriori algorithm to search for combinations of genes that are frequently identifed as having harmful mutations in individuals with the disease phenotype. The apriori algorithm may also be used to identying combinations of alleles that are frequently identified in individuals with the disease phenotype. 

## Features
This program generates a web-server that allows the user to upload a `.vcf` file and analyze it using several tools ([Open-Cravat](https://github.com/KarchinLab/open-cravat/wiki), [ANNOVAR](http://annovar.openbioinformatics.org/en/latest/), and some custom scripts.)
## Pre-Requisites
Need to have Python >= 3.5. Install most of the prerequisites through `pip`:
```
pip3 install open-cravat flask efficient-apriori pandas
cravat-admin install-base
```
Download and install [ANNOVAR](http://annovar.openbioinformatics.org/en/latest/user-guide/download/).

## Running the Program
Move the `.vcf` files into the `/webapp/` directory.
If you have e.g. `python3.7`, run `python3.7 hello.py`. This will start the web-server on `http://localhost:5000/`.

## Program Logic and Design
![project overview](https://github.com/NCBI-Hackathons/pheno_geno_ataxia/blob/master/programFlow.png "Logo Title Text 1")

## Future work
Gene ontology over-representation analysis on genes or variants identifed as likely harmful.
Filtering out variants in linkage-disequilibrium.
Interactive variant filtering. 
Saving results in a database.
Incorporate genomic information from family members.
