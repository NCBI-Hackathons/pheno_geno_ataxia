#!/usr/bin/env python3
import pandas as pd
import csv
def get_apriori_input(input_file,output_file,sample_col="Sample",gene_id_col="Gene_ID"):
    df=pd.read_csv(input_file,sep="\t")
    sample_names=df[sample_col].unique()
    with open(output_file,"w") as out:
        csv_writer=csv.writer(out,delimiter="\t")
        for sample_name in sample_names:
            bool=df[sample_col]==sample_name
            df_sample=df[bool]
            gene_ids=df_sample[gene_id_col]
            gene_string=",".join(gene_ids)
            csv_writer.writerow([sample_name,gene_string])


if __name__ == "__main__":
    import sys
    program,input_file,output_file,sample_col,gene_id_col=sys.argv
    get_apriori_input(input_file,output_file,sample_col,gene_id_col)
