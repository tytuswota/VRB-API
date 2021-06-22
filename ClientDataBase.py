
class ClientDataBase():
    def __init__(self):
        self.data = []
        
    def storeData(self, data, mysql):

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO measurement(type, measurement) VALUES (%s, %s)", (data[1], data[2]))
        mysql.connection.commit()
        cur.close()

        print('here the data will be stored....')
        return 200
    
    def updateStatus(self, data, mysql):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE devices SET status = %s WHERE id = %s", (data[1], data[0]))
        mysql.connection.commit()
        cur.close()

        print('here the data will be stored....')
        return 200