# Phenotype_Genotype_Ataxia
## Features
This program generates a web-server that allows the user to upload a `.vcf` file and analyze it using several tools ([Open-Cravat](https://github.com/KarchinLab/open-cravat/wiki), [ANNOVAR](http://annovar.openbioinformatics.org/en/latest/), and some custom scripts.)
## Pre-Requisites
Need to have Python > 3.5.
Install Open-Cravat, ANNOVAR, Flask.
Requires the python package efficient-apriori which can be installed with: pip install efficient-apriori

## Running the Program
Move the `.vcf` files into the `/webapp/` directory.
If you have e.g. `python3.7`, run `python3.7 hello.py`. This will start the web-server on `http://localhost:5000/`.
