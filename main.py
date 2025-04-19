#MapPlot.py
#Name:
#Date:
#Assignment:

import video_games
import pandas
import matplotlib.pyplot as plt
video_game = video_games.get_video_game()

#print(video_game[0]["Length"]["Main Story"])
ratings = []
time_Playings = []

for Sales in video_game:
    Ratings = Sales["Metrics"]["Review Score"]
    Time_Playing = Sales["Length"]["Main Story"]["Average"]
    if 50 <= Ratings <= 100 and Time_Playing <= 60: # cleaning of plots to include only games with decent reviews scores or average play time
       ratings.append(Ratings)
       time_Playings.append(Time_Playing) 
    #print(Ratings,Time_Playing)
print(ratings)
df = pandas.DataFrame({
    "Ratings": ratings, 
    "Time_Playing": time_Playings
})
df.plot(kind='scatter', x='Ratings', y='Time_Playing')
if Ratings > 80:
  plt.plot(ratings, time_Playings, 'ro')
  
else:
  plt.plot(Ratings, Time_Playing, 'ko')


plt.title("Ratings vs Main Story Time")
plt.xlabel("Review Score")
plt.ylabel("Main Story Play Time (hrs)")
plt.savefig("output")
plt.show()