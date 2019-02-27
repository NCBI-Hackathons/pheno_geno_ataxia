import random
import pandas as pd
import numpy as np
import networkx as nx
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt

def create_rules():

    fname = './Sample_Data/sample_variants.txt'
    dataset = []
    with open(fname, 'r') as fhandle:
        lines = fhandle.readlines()
        for line in lines:
            if len(line) > 0:
                patientid, genes = line.split('\t')
                genes = genes.split(',')
                tmp = genes[-1]
                tmp = tmp[0:len(tmp) - 1]
                genes[-1] = tmp
                dataset.append(genes)
    print(dataset)
    oht = OnehotTransactions()
    oht_ary = oht.fit(dataset).transform(dataset)
    df = pd.DataFrame(oht_ary, columns=oht.columns_)
    frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
    association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
    return rules

def draw_graph(rules, rules_to_show):

    G1 = nx.DiGraph()
    color_map=[]
    N = 50
    colors = np.random.rand(N)
    strs=['R0', 'R1']

    for i in range (rules_to_show):
        confidence = '(' + str(rules.iloc[i]['confidence']) + ')'
        G1.add_nodes_from(["R"+str(i)])

        for a in rules.iloc[i]['antecedents']:
            G1.add_nodes_from([a])
            G1.add_edge(a, "R"+str(i), color=colors[i] , weight = 2)

        for c in rules.iloc[i]['consequents']:
            G1.add_nodes_from([c])
            G1.add_edge("R"+str(i), c, color=colors[i],  weight=2)

    for node in G1:
        found_a_string = False
        for item in strs:
            if node==item:
                found_a_string = True
        if found_a_string:
            color_map.append('yellow')
        else:
            color_map.append('green')

    edges = G1.edges()
    colors = [G1[u][v]['color'] for u,v in edges]
    weights = [G1[u][v]['weight'] for u,v in edges]

    pos = nx.spring_layout(G1, k=16, scale=1)
    nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16, with_labels=False)

    for p in pos:  # raise text positions
        pos[p][1] += 0.07
    nx.draw_networkx_labels(G1, pos)
    plt.show()
def main():
    rules = create_rules()
    print(rules.to_string())
    draw_graph (rules, 2)

main()
