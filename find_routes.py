import airport_data as apd
import airlines_data as ald
import networkx as nx
import graph as g

H = g.G.copy()

def find_airports(city):
    airports = []
    source_df = apd.airports_df[apd.airports_df['City'] == city]
    for i, row in source_df.iterrows():
        #     print(source_df.at[i, 'ID'])
        airports.append(source_df.at[i, 'ID'])
    return airports


# find_airports(source)


def find_shortest_paths(source_city, dest_city):
    source_airports = find_airports(source_city)
    dest_airports = find_airports(dest_city)

    #     print(source_airports)
    #     print(dest_airports)

    shortest_len = 100
    shortest_paths = []
    sp = []

    for s_node in source_airports:
        s_node = s_node.astype(str)
        for d_node in dest_airports:
            d_node = d_node.astype(str)
            #         print('d', d_node, H.has_node(d_node.astype(str)))
            #         print('s', s_node, H.has_node(s_node.astype(str)))
            #         print(H.has_node(d_node.astype(str)) and H.has_node(s_node.astype(str)))
            if (H.has_node(d_node.astype(str)) and H.has_node(s_node.astype(str))):
                sh = nx.shortest_path_length(H, s_node, d_node)
                #             print('sh', sh)
                if sh <= shortest_len:
                    shortest_len = sh
                    shortest_paths.append(nx.all_shortest_paths(H, s_node, d_node))
    for i in shortest_paths:
        for x in i:
            #         print('x', x)
            #         print(shortest_len)
            if len(x) == shortest_len + 1:
                exists = True
                for ap in x:
                    exists = ((apd.airports_df['ID'] == int(ap)).any() and exists)

                if exists:
                    sp.append(x)
    return sp


def calc_airport_range(airport, airport_weights_dic):
    #     ap = 3941
    final_weight = 0
    #     print(ap)

    for column in list(apd.airport_rated)[3:14]:
        try:
            rate = apd.airport_rated[apd.airport_rated['ID'] == airport][column].values[0]
        except:
            if (column == 'Passengers 2016'):
                rate = 0
            #                 print(rate)
            rate = 3
        weight = airport_weights_dic[column]
        final_weight += rate * weight
    return final_weight


def calc_airline_range(src, dst, airlines_weights_dic):
    #     print(H.has_edge(src, dst))
    #     print(H[src][dst])
    route_data = H[src][dst]
    final_ratings = []
    for route in route_data.values():
        #         print(route)
        airline = route['Airline ID']
        #         print(airline)

        #         print(airlines_df[airlines_df['ID'] == airline]['Name'].values[0])

        final_rating = 0
        for column in list(ald.airlines_rated)[3:12]:
            try:
                rate = ald.airlines_rated[ald.airlines_rated['ID'] == int(airline)][column].values[0]
            #                 print(column)

            except:
                rate = 3
            weight = airlines_weights_dic[column]
            final_rating += rate * weight
        final_ratings.append(final_rating)
    #     print(final_ratings)
    return max(final_ratings)

# zwraca znalezione ścieżki w postaci:
# {ocena : [lista lotnisk]}
def rate_sorted_paths(source_city, dest_city, airport_weights_dic, airlines_weights_dic):
    paths = find_shortest_paths(source_city, dest_city)
    rated_routes = {}

    for path in paths:
        ap_rate = 0
        al_rate = 0
        transfers = path[1:-1]
        #         print(transfers)
        for airport in transfers:
            ap_rate += calc_airport_range(int(airport), airport_weights_dic)
        #             print('rate', rate)

        #         print([x for x in range(len(path))])
        for i in range(len(path) - 1):
            al_rate += calc_airline_range(path[i], path[i + 1], airlines_weights_dic)
        #         print(al_rate/(len(path)-1))
        # srednia ocena wszystkich najlepszych linii na trasie
        rate = ap_rate / 50 + al_rate / 45

        rated_routes[rate] = path
    return rated_routes


def get_sorted_paths(source_city, dest_city, airport_weights_dic, airlines_weights_dic):
    routes = rate_sorted_paths(source_city, dest_city, airport_weights_dic, airlines_weights_dic)
    sorted_paths = []
    for k, v in sorted(routes.items(), reverse=True):
        cities = []
        #         pos = {}
        for airport in v:
            #             print(airport)
            try:
                city = apd.airports_df.loc[apd.airports_df['ID'] == int(airport), 'City'].values[0]
                name = apd.airports_df.loc[apd.airports_df['ID'] == int(airport), 'Name'].values[0]
            except:
                print(airport)
            #             print("{}, {}".format(city, name))
            cities.append("{}, {}".format(city, name))
        cities.append(k)
        sorted_paths.append(cities)
    return sorted_paths