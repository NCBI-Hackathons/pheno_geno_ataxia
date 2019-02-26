def combine_tables_in_dir(directory,outfile,split_str_for_sample_name="."):
    import os
    import pandas as pd
    files=os.listdir(directory)
    tables=[]
    for file in files:
        sample_name=file.split(split_str_for_sample_name)[0]
        print sample_name
        infile=directory.rstrip("/")+"/"+file
        df=pd.read_csv(infile,sep="\t")
        df["Sample"]=sample_name
        tables.append(df)

    df_cat=pd.concat(tables)
    df_cat.to_csv(outfile,sep="\t",index=False)

if __name__ == "__main__":
	import sys
	program,directory,outfile,split_str_for_sample_name=sys.argv
	combine_tables_in_dir(directory,outfile,split_str_for_sample_name)
