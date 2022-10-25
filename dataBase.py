import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")

        cursor = connection.cursor()
        query = ("SELECT * FROM category_description;")
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()

    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("5.183.188.132", "db_vgu_student", "thasrCt3pKYWAYcK", "db_vgu_test2")
connection.close()

