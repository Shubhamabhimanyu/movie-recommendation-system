from getpass import getpass
import pandas as pd
class login:
	def __init__(self):
		self.__option = str(input('Do You have an account (y/n): ')).lower()
		if(self.__option == 'y'):
			self.__loginTakeInput()
			self.__loginStatus = self.__checkUser()

	def __loginTakeInput(self):
		self.__email = str(input('Please Enter your Email: ')).lower()
		if(bool(self.__email) != False):
			self.__password = getpass()

	def __checkUser(self):
		df = pd.read_csv("user.csv")
		useremail = df.loc[(df['useremail'] == self.__email)]
		if(not useremail.empty):
			password = df.loc[(df['useremail'] == self.__email)]['password'].values[0]
			if(self.__password == password):
				return True
			return False
		return False

	def getLoginStatus(self):
		return self.__loginStatus
