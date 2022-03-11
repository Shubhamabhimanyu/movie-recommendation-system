import login
import movie_recommender

if __name__ == '__main__':
	loginStatus = login.login().getLoginStatus()
	if(loginStatus):
		movie_recommender.movie_recommend()
	else:
		print('Sorry!! You have entered wrong details')
