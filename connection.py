import pymysql.cursors  

class dbConnection:
        def __init__(self):
                self.connection = self.__getConnection()

        def __getConnection(self):
                connection = pymysql.connect(host='localhost', user='root', password='', db='movie_recommendation', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                return connection

        def fetchData(self, table, columns = ['*'], condition = {1:1}):
                connection = self.connection
                if (type(table) is str):
                        if(type(columns) is list):
                                columns = ', '.join(columns)
                                if(type(condition) is dict):    
                                        condition = ' AND '.join(str(k) + " = '" + str(v) +"'" for k, v in condition.items())                                 
                                        try:
                                                with connection.cursor() as cursor:
                                                        sql = "SELECT "+ columns +" FROM "+ table + " WHERE " + condition
                                                        cursor.execute(sql)
                                                        print ("cursor.description: ", cursor.description)
                                                        print()
                                                        for row in cursor:
                                                                print(row)
                                        finally:
                                                pass
                                else:
                                        print('Columns should be of dict datatype')
                        else: 
                                print('Column Details should be of list datatype')
                else:
                        print('Table Name Should be of string type')

        def insertData(self, table, details):
                connection = self.connection
                if type(table) is str:
                        if type(details) is dict:
                                details = ', '.join(str(k) + " = '" + str(v) + "'" for k, v in details.items())
                                cursor = connection.cursor()
                                try:    
                                        sql = "INSERT INTO "+ table +" set "+ details
                                        cursor.execute(sql)
                                        connection.commit()
                                finally:
                                        pass
                        else: 
                                print('Details should be of dict type')
                else:
                        print('Table Name Should be of string type')

if __name__ == '__main__':
        db = dbConnection()
        db.insertData('user', {'user_name': 'Sunny Gupta', 'movie_watched' : 1})
        db.fetchData('user')
