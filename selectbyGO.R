# 2/26/19
# Author: Jenna Oberstaller

# extracting genes based on GO categories of interest and writing to file

# load required packages

library(AnnotationDbi)
library(org.Hs.eg.db)
library(topGO)
library(GO.db)


# CAN EASILY BE UPDATED to extract (or exclude) any of the following additional information

# > columns(org.Hs.eg.db)
#[1] "ACCNUM"       "ALIAS"        "ENSEMBL"      "ENSEMBLPROT"  "ENSEMBLTRANS"
#[6] "ENTREZID"     "ENZYME"       "EVIDENCE"     "EVIDENCEALL"  "GENENAME"    
#[11] "GO"           "GOALL"        "IPI"          "MAP"          "OMIM"        
#[16] "ONTOLOGY"     "ONTOLOGYALL"  "PATH"         "PFAM"         "PMID"        
#[21] "PROSITE"      "REFSEQ"       "SYMBOL"       "UCSCKG"       "UNIGENE"     
#[26] "UNIPROT"  

GO.ids.to.genes <- function(GO.term.list){
  
  keys = GO.term.list
  specific.GO.db = select(org.Hs.eg.db, keys = keys, columns = c("SYMBOL", "GENENAME", "PATH"), keytype = "GO")
  
  write.table(specific.GO.db, "GOtoGenes.tab.txt", row.names = FALSE, sep = "\t", quote = FALSE)
  
}
