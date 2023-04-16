import csv
from collections import Counter

musicData = 'formatted-v7_2017-2021_Spotify_Top_200.csv'
genresCount = {}

# opening the CSV file
with open(musicData, mode ='r') as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:

        year = lines[4][:4]
        if year == '2020':
            genres = lines[5].split(';;')
            # print(year, genres)

            # count genres
            for genre in genres:
                genresCount[genre] = genresCount.get(genre, 0) + 1

topHundredGenres = dict(sorted(genresCount.items(), key=lambda x:x[1], reverse=True)[:100])
print(topHundredGenres)
