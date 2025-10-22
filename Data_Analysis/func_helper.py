import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

EDGE_SIZE = {
    'comesAfter': 2,
    'isPartOf': 1,
}

EDGE_COLOR = {
    'comesAfter': 'purple',
    'isPartOf': 'red',
}

def open_file(filepath):
    df = pd.read_csv(filepath)
    df.set_index('identifier', inplace=False)

    return df

def clean_edge(edge):
    s.edge[edge[0], edge[1]].values()

def c_(list_edges): return [a for a in list_edges if a in list(EDGE_COLOR.keys())]

# For nx.Graph()
def edge_sizes(s):
    print(s)
    print([EDGE_SIZE[c_(list(s.edges[edge[0], edge[1]].keys()))[-1]] for edge in
                           s.edges()])
    input("Press enter to continue...")

    return [EDGE_SIZE[c_(list(s.edges[edge[0], edge[1]].keys()))[-1]] for edge in
                           s.edges()]  # /!\ multiple links => one size

def edge_colors(s):
    print([EDGE_COLOR[c_(list(s.edges[edge[0], edge[1]].keys()))[-1]] for edge in
                            s.edges()])
    input("Press enter to continue...")
    return [EDGE_COLOR[c_(list(s.edges[edge[0], edge[1]].keys()))[-1]] for edge in
                            s.edges()]  # /!\ multiple links => one color

def draw(df, G, s):
    pos = nx.spring_layout(s, scale=0.5)
    node_labels = dict((n, df['title']) for n, d in s.nodes(data=True))
    #     labels = {**node_labels, **edge_labels}
    nx.draw(s, pos=pos, width=edge_sizes(s), edge_color=edge_colors(s), alpha=0.8, arrows=False, node_color='lightgrey',
            node_size=400,
            labels=node_labels,
            font_color='black', font_size=8, font_weight='bold',
            )
    edge_labels = dict(((u, v), list(d.values())[0]) for u, v, d in G.edges(data=True))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# identifier	title	description	url	type	isPartOf	assesses	comesAfter	requires	alternativeContent	references	isFormatOf
def build_graph(df):
    column_edge = 'comesAfter'
    column_ID = 'identifier'

    df_topic = df[df[column_edge].notna()]

    print(df_topic)

    G = nx.from_pandas_edgelist(
        df_topic,
        source=column_ID,
        target=column_edge,
        edge_attr='title'
    )


    print(G)

    input("Press enter to continue...")
    nx.set_node_attributes(G, {row[column_ID]: {'Name': row['title']} for i, row in
                               df_topic.iterrows()})


    # input("Press enter to continue...")
    draw(df_topic, G, nx.ego_graph(G=G, n=1, radius=3))

    # nx.draw(G)
    # plt.show()

    return G