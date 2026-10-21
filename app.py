import streamlit as st
from pages1.Utils1.sample_data import sample_ppr_nodes, sample_ppr_edges
from pages1.Utils1.graphUtils import nx_Digraph, nx_to_yfiles_graph, show_yfiles_graph
from pages1.Utils1.config import global_nodes_list, VIEW_ATTRS_MAPPING
from pages1.Utils1.data_transform import (
    nodes_by_class, edges_by_type, extract_numeric,
    are_attributes_same, remove_links_of_node,
)

st.set_page_config(page_title="PPR Visualizer", layout="wide")
st.title("PPR Visualizer")

# ---- Step 1: graph ----
G = nx_Digraph(sample_ppr_nodes, sample_ppr_edges)
nodes, edges = nx_to_yfiles_graph(G)
show_yfiles_graph(nodes, edges)

# ---- Step 2: config test ----
st.subheader("config test")
st.write(global_nodes_list)
st.write(list(VIEW_ATTRS_MAPPING["Engineering View"]["Resource"].keys()))

# ---- Step 2: data_transform test ----
st.subheader("data_transform test")
st.write(nodes_by_class(sample_ppr_nodes))
st.write(edges_by_type(sample_ppr_edges))
st.write(extract_numeric("12.5 kg"), extract_numeric("abc"))
st.write(are_attributes_same({"product_cost": 20.0}, [{"attr_name": "product_cost", "value": "20.0 Euro"}]))
st.write(are_attributes_same({"product_cost": 20.0}, [{"attr_name": "product_cost", "value": "25.0 Euro"}]))
links = [{"source": "A", "target": "B"}, {"source": "B", "target": "C"}, {"source": "C", "target": "D"}]
remove_links_of_node(links, "B")
st.write(links)