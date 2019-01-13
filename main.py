import find_routes as fr
import airport_data as apd
import airlines_data as ald

# testowe dane
airport_weights_dic = dict(zip(list(apd.airport_rated)[3:14], [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1]))
airlines_weights_dic = dict(zip(list(ald.airlines_rated)[3:12], [5, 3, 3, 3, 3, 3, 3, 3, 1]))
source = "Warsaw"
dest = "Montreal"

# print(fr.rate_sorted_paths(source, dest, airport_weights_dic, airlines_weights_dic))
print(fr.get_sorted_paths(source, dest, airport_weights_dic, airlines_weights_dic))


