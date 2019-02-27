import pandas as pd
infile="/home/justin/pheno_geno_ataxia/Sample_Data/Combine_Tables/combined_annovar_output.txt"
outfile="/home/justin/pheno_geno_ataxia/Sample_Data/Combine_Tables/combined_annovar_output_08filtered.txt"

def convertable_to_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def filter_on_polypen(infile,min_score=1):
    df=pd.read_csv(infile,sep="\t",comment='#')
    polyphen_column="Polyphen2_HDIV_score"
    df=df[df[polyphen_column].apply(lambda x: convertable_to_float(x))]
    df[polyphen_column]=pd.to_numeric(df.Polyphen2_HDIV_score)
    v_bool=df[polyphen_column]>=min_score
    df_return=df[v_bool]
    df_return.to_csv(outfile,sep="\t",index=False)



filter_on_polypen(infile)
