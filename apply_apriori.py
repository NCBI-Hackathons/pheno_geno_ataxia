#!/usr/bin/env python3

def get_data_from_file(input_file):
	import csv
	flagged=[]
	with open(input_file,"r") as in_file:
		csv_reader=csv.reader(in_file,delimiter="\t")
		for row in csv_reader:
			if len(row) >0:
				gene_string=row[1]
				gene_tuple=tuple(gene_string.strip().split(","))
				flagged.append(gene_tuple)		
	return flagged

def apply_approri(data,min_support=0.5,min_confidence=1):
	from efficient_apriori import apriori
	items,rules=apriori(data,min_support=min_support,min_confidence=min_confidence)
	return(items,rules)


def pull_out_association(rule_string):
	components=rule_string.split()
	association="".join(components[:3])
	
	return association

def format_appriori_output(rules,outfile):
	import csv
	header=["association","confidence","support","lift","conviction"]

	with open(outfile,"w") as out:
		writer=csv.DictWriter(out,fieldnames=header,delimiter="\t")
		writer.writeheader()
		for rule in rules:
			relationship=str(rule)
			association=pull_out_association(relationship)
			confidence=rule.confidence
			support=rule.support
			lift=rule.lift
			conviction=rule.conviction
			row=[association,confidence,support,lift,conviction]
		
			row_dict=dict(zip(header,row))

			writer.writerow(row_dict)


def main(input_file,outfile,min_support=0.5,min_confidence=1):

	flagged_genes=get_data_from_file(input_file)
	items,rules=apply_approri(flagged_genes)

	format_appriori_output(rules,outfile)


if __name__== "__main__":
	import sys
	program,input_file,min_support,min_confidence,outfile=sys.argv

	main(input_file, outfile, float(min_support), float(min_confidence))	
