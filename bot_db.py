import pymysql
import datetime


def create_mysql_connection():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'shubhamraj8006',
        'db': 'botsearch'
    }
    connection = pymysql.connect(**config)
    return connection


def save_search_keyword(userid, keyword):
    connection = create_mysql_connection()
    cursor = connection.cursor()
    curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO search_result VALUES('{}', '{}', '{}')".format(userid, keyword, curr_time)
    cursor.execute(query)
    connection.commit()
    connection.close()



def get_recent_search_data(userid, keyword):
    connection = create_mysql_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM search_result WHERE userid = {0} AND keyword LIKE '%{1}%'".format(userid, keyword)
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.close()
    return result