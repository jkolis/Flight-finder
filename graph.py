import networkx as nx
import pandas as pd
import utilities as u
import airport_data as apd

route_cols = ['Airline', 'Airline ID', 'Source Airport', 'Source ID',
              'Dest Airport', 'Dest ID', 'Codeshare', 'Stops', 'Equipment']
routes_df = pd.read_csv("data/routes.dat", names = route_cols)

routes_df = routes_df[routes_df['Source ID'].apply(u.is_number)]
routes_df = routes_df[routes_df['Dest ID'].apply(u.is_number)]

G = nx.from_pandas_edgelist(routes_df, source='Source ID',
                            target='Dest ID', edge_attr=['Airline ID'],
                            create_using=nx.MultiDiGraph())

lat = apd.airports_df.filter(['ID', 'Lat'], axis=1)
lat['ID']= lat['ID'].astype(str)
lat_dic = lat.set_index('ID')['Lat'].to_dict()

long = apd.airports_df.filter(['ID','Long'], axis=1)
long['ID']= long['ID'].astype(str)
long_dic = long.set_index('ID')['Long'].to_dict()

nx.set_node_attributes(G, values=lat_dic, name="lat")
nx.set_node_attributes(G, values=long_dic, name="long")