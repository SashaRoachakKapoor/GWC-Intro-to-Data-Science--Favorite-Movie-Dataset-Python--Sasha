#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Zootopia"
print("my favorite movie is: "+favMovie)

#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
MovieTrue= movieData["movie_title"] == favMovie
favMovieData= movieData.loc[MovieTrue]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre
genreTrue = movieData["genres"].str.contains("Action & Adventure")
genreChosen = movieData.loc[genreTrue]

numOfMovies = genreChosen.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Action & Adventure in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Action & Adventure.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = genreChosen["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 92 points higher than the lowest rated movie.")
print()

#find max
max = genreChosen["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 6 points lower than the highest rated movie.")
print()

#find mean
mean = genreChosen["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = genreChosen["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(genreChosen["audience_rating"], range = (10,100), bins = 20 )

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Action & Adventure Histogram")
plt.xlabel("Audience Rating")
plt.ylabel("Number of Action & Adventure Movies")

#Prints interpretation of histogram
print(
  " The data is continous, so a histogram is the best representation for this. According to the histogram, around 260 action and adventure movies had an audience rating of 50, which is the highest number of movies, given the ratings. We can also see that there were no movies with a rating between 0 to 10. Moreover, majority of action and advenure movies had an overall high rating above 50%. The median audience rating is greater than the median rating. This means that the audience rating for action and adventure movies is positively skewed. "
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

#Create scatterplot
plt.scatter(data = genreChosen, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, as more movies had a higher audience rating, the critic rating also increased. This means that there is a positive correlation. However, there are some outliers that don't match the trend of the data, so the data might have a weak positive correlation."
)
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
