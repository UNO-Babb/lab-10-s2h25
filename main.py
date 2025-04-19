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

#The charts/visualization showed how critics review scores related to the average playing time for the main story of video games.  In a attempt to clean up the plotting, I helped it focus on review scores between 50-100 and playing time under 60 hours.  A few patterns revealed that some of the highest rated games are not necessarily the longest, play time does not guarantee quality, and most games under 20 hours received top review scores. 