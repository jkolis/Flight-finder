import pandas as pd
import utilities as u

airport_col = ['ID', 'Name', 'City', 'Country','IATA', 'ICAO', 'Lat', 'Long', 'Alt', 'Timezone', 'DST', 'Tz database time zone', 'type', 'source']
airports_df = pd.read_csv("data/airports.dat", names=airport_col)

airport_rev = pd.read_csv('data/airport.csv')

air_map_col = ['code', 'airport_name', 'Name']
airport_mapping = pd.read_csv('data/airports_map.dat', names=air_map_col)

passengers = pd.read_excel('data/pass.xlsx')

merged1 = pd.merge(airport_mapping, airport_rev, how='inner', on='airport_name')
merged2 = pd.merge(merged1, airports_df, how='inner', on="Name")
merged_airports = pd.merge(merged2, passengers, how='left', on='Name')
merged_airports = merged_airports.drop(columns=['link', 'title', 'author', 'author_country',
                                                'content', 'date', 'experience_airport', 'date_visit',
                                                'type_traveller', 'IATA', 'Alt',
                                                'Timezone', 'DST', 'Tz database time zone', 'type',
                                                'source', 'Country'])

merged_airports['Passengers 2016'].fillna(0, inplace=True)
merged_airports['overall_rating'].fillna(5, inplace=True)
merged_airports.fillna(3, inplace=True)

airport_rated = pd.DataFrame(columns=list(merged_airports))
count = 0
for airport in merged_airports['airport_name'].unique():
    temp = merged_airports.loc[merged_airports['airport_name'] == airport]
    #     print(temp.iloc[[0]])
    airport_rated.loc[count] = temp.iloc[0]
    u.set_mean(airport_rated, temp, count, list(merged_airports)[3:13])
    count += 1

u.scale_ratings(airport_rated, list(airport_rated)[4:12], 2)
u.scale_ratings(airport_rated, ['recommended'], 10)
u.scale_ratings(airport_rated, ['Passengers 2016'], 10/101491106)

airport_rated = airport_rated[['code', 'airport_name', 'Name', 'overall_rating', 'queuing_rating', 'terminal_cleanliness_rating', 'terminal_seating_rating', 'terminal_signs_rating', 'food_beverages_rating', 'airport_shopping_rating', 'wifi_connectivity_rating', 'airport_staff_rating', 'recommended', 'Passengers 2016', 'ID', 'City', 'ICAO', 'Lat', 'Long']]





