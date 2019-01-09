import pandas as pd
import utilities as u

airlines_col = ['ID', 'Name', 'Alias', 'IATA', 'ICAO', 'Callsign', 'Country', 'Active']
airlines_df = pd.read_csv('data/airlines.dat', names=airlines_col)

airlines_rev = pd.read_csv('data/airline.csv')

airlines_map_col = ['code', 'airline_name', 'Name']
airlines_mapping = pd.read_csv('data/airlines_map.dat', names=airlines_map_col)

merged_airlines1 = pd.merge(airlines_mapping, airlines_rev, on='airline_name')
merged_airlines = pd.merge(merged_airlines1, airlines_df, on='Name')
merged_airlines = merged_airlines.drop(columns=['link', 'title', 'author', 'author_country',
                                                'content', 'date', 'aircraft', 'type_traveller',
                                                'cabin_flown', 'route', 'Alias', 'Callsign', 'Active'])

merged_airlines['overall_rating'].fillna(5, inplace=True)
merged_airlines.fillna(3, inplace=True)

airlines_rated = pd.DataFrame(columns=list(merged_airlines))
count = 0
for airline in merged_airlines['airline_name'].unique():
    temp = merged_airlines.loc[merged_airlines['airline_name'] == airline]
    #     print(temp.iloc[[0]])
    airlines_rated.loc[count] = temp.iloc[0]
    u.set_mean(airlines_rated, temp, count, list(merged_airlines)[3:12])
    count += 1


u.scale_ratings(airlines_rated, list(airlines_rated)[4:11], 2)
u.scale_ratings(airlines_rated, ['recommended'], 10)



