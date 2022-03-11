import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class movie_recommend(object):
	def __init__(self):
		self.movie_name = str(input("Enter you favourite Movie Name: ")).title()
		if(bool(self.movie_name) != False):
			searchBy = False
			count = 0
			while(not searchBy and count < 4):
				count+=1
				print("Note: You can give more than 1 option by seperation with space")
				self.searchBy = str(input("Enter Your search by option:\n\
1 for Genre\n\
2 for Cast\n\
3 for Director\n\
4 for Keywords\n")).strip()
				try:
					self.searchBy = np.unique(self.searchBy.split(' ')).astype(np.int)
					if(max(self.searchBy) < 4 and min(self.searchBy)> 0):
						searchBy = True
				except:
					print('Please Enter the Details Correctly')
		if(searchBy):
			self.df = pd.read_csv("movie_dataset.csv")
			self.__getMovie()

	def __searchBy(self, gid):
		return {1 : 'Genres', 2 : 'Cast', 3 : 'Director', 4 : 'Keywords'}.get(gid)

	def __getSearchBy(self, idArray):
		searchArray = []
		for gid in idArray:
			searchArray.append(self.__searchBy(gid))
		return searchArray

	def __get_title_from_index(self, index):
		return self.df[self.df.index == index]["title"].values[0]

	def __get_index_from_title(self, title):
		return self.df[self.df.title == title]["index"].values[0]

	def __combine_features(self, row):
		try:
			output = []
			for keyword in self.__getSearchBy(self.searchBy):
				output.append(row[keyword.lower()])
			return " ".join(output)
		except:
			print("Error:", row)
	
	def __getMovie(self):
		features = ['keywords','cast','genres','director']
		for feature in features:
			self.df[feature] = self.df[feature].fillna('')
		self.df["combined_features"] = self.df.apply(self.__combine_features,axis=1)
		cv = CountVectorizer()
		count_matrix = cv.fit_transform(self.df["combined_features"])
		cosine_sim = cosine_similarity(count_matrix) 
		movie_user_likes = self.movie_name
		movie_index = self.__get_index_from_title(movie_user_likes)
		similar_movies =  list(enumerate(cosine_sim[movie_index]))
		sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
		i=0
		for element in sorted_similar_movies:
			print(self.__get_title_from_index(element[0]))
			i=i+1
			if i > 5:
				break
