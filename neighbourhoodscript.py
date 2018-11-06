import pandas as pd
import requests

anti_social_crime = pd.read_csv('anti_social_crime.csv')
for index, row in anti_social_crime.iterrows():
	if (pd.isnull(row['Neighbourhood'])):
		longitude = row['Longitude']
		latitude = row['Latitude']
		url = f'https://data.police.uk/api/locate-neighbourhood?q={latitude},{longitude}'
		response = requests.get(url)
		try:
			neighbourhood = response.json()['neighbourhood']
			anti_social_crime.at[index, 'Neighbourhood'] = neighbourhood
		except:
			 print('Longitude: ' + str(longitude))
			 print('Latitude: ' + str(latitude))
		#if (index % 1000 == 0):
anti_social_crime.to_csv('anti_social_crime.csv', index=False)
