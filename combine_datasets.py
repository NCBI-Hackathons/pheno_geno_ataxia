import pandas as pd

def combine_tables_in_dir(directory,outfile,split_str_for_sample_name="."):
    import os
    import pandas as pd
    files=os.listdir(directory)
    tables=[]
    for file in files:
        sample_name=file.split(split_str_for_sample_name)[0]
        #print sample_name
        infile=directory.rstrip("/")+"/"+file
        df=pd.read_csv(infile,sep="\t",comment='#')
        df["Sample"]=sample_name
        tables.append(df)

    df_cat=pd.concat(tables)
    df_cat.to_csv(outfile,sep="\t",index=False)

def join_annotation_files(annovar_file,open_cravat_file):
    df_annovar=pd.read_csv(annovar_file,sep="\t",comment='#')
    df_cravat=pd.read_csv(open_cravat_file,sep="\t",comment="#")

    df_merge=df_annovar.merge(df_cravat,on=["Gene.refGene","Hugo"],how="inner",suffixes=["annovar_","cravat_"])

    print(df_merge[:5])

annovar_tables="/home/justin/pheno_geno_ataxia/Sample_Data/Annovar_Tables"
cravat_tables="/home/justin/pheno_geno_ataxia/Sample_Data/Cravat_Tables"
outdir="/home/justin/pheno_geno_ataxia/Sample_Data/Combine_Tables"

def main(annovar_tables,cravat_tables,outdir):
    annovar_split_string=".vcf.txt"
    annovar_outfile=outdir+"/combined_annovar_output.txt"
    combine_tables_in_dir(annovar_tables,annovar_outfile,annovar_split_string)

    cravat_split_string=".vcf.tsv"
    cravat_outfile=outdir+"/combined_cravat_outfile.txt"
    combine_tables_in_dir(cravat_tables,cravat_outfile,cravat_split_string)

    join_annotation_files(annovar_outfile,cravat_outfile)
main(annovar_tables,cravat_tables,outdir)
