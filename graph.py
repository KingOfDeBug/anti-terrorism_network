from networkx import Graph
import matplotlib.pyplot as plt
import networkx as nx

class  my_graph(Graph):
    def plot(self,country_dict, edge_weight = False):
        plt.rcParams['figure.figsize'] = (8, 6)
        edges,weights = zip(*nx.get_edge_attributes(self,'weight').items())
        pos = nx.spring_layout(self)
        nx.draw(self, pos,  edgelist=edges, edge_color=weights, width=10.0, edge_cmap=plt.cm.Blues,with_labels = False)
        node_label = self.get_node_label(country_dict)
        nx.draw_networkx_labels(self,pos,node_label)
        if edge_weight:
            labels = {e: self.edges[e]["weight"] for e in self.edges}
            nx.draw_networkx_edge_labels(self, pos, edge_labels=labels)
        plt.savefig('graph.png')

    def get_node_label(self,country_dict):
        return  {e:country_dict[int(e)][0] for e in self.nodes}

