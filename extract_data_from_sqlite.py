import sqlite3
import pandas as pd
def sqlite_to_tsv(dbfile,outfile):
    conn=sqlite3.connect(dbfile)
    df=pd.read_sql_query("select * from gene;",conn)
    df.to_csv(outfile,sep="\t")

if __name__== "__main__":
    import sys
    program,dbfile,outfile=sys.argv
sqlite_to_tsv(dbfile,outfile)
