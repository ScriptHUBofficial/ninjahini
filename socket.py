import socket
from threading import Thread
import pymysql
import time

def client_handler(conn):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         db='101m',)
    baglanti = db.cursor()
    
    try:
        while True:
    
            data = conn.recv(1024).decode("utf-8")
            print(data)
            if not data:
                print("server is down")
                break

        
            data_list = data.split('|')


            query = "SELECT * FROM `101m` WHERE "
            where_clauses = []
            
            if len(data_list[0]) != 0:
                where_clauses.append(f"`ADI` LIKE '{data_list[0]}'")
            if len(data_list[1]) != 0:
                where_clauses.append(f"`SOYADI` LIKE '{data_list[1]}'")
            if len(data_list[2]) != 0:
                where_clauses.append(f"`DOGUMTARIHI` LIKE '{data_list[2]}'")
            if len(data_list[3]) != 0:
                where_clauses.append(f"`NUSUFIL` LIKE '{data_list[3]}'")
            if len(data_list[4]) != 0:
                where_clauses.append(f"`TC` LIKE '{data_list[4]}'")
            
            if len(where_clauses) > 0:
                query += " AND ".join(where_clauses)
                baglanti.execute(query)
                kullanicilar = baglanti.fetchall()
            else:
                kullanicilar = []
        
            for i in kullanicilar:
                time.sleep(0.1)
                i = list(i)
                i[0] = str(i[0])
                bilgi = '|'.join(i)
                print(bilgi)
                conn.send(bilgi.encode("utf-8"))
        
        
        conn.close()

    except ( ConnectionAbortedError,ConnectionResetError ):
        pass



def server_program():
    host = "127.0.0.1"
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
 
    while True:
        conn, address = server_socket.accept()
        print("BAGLANTİ: " + str(address))


        Thread(target=client_handler, args=(conn,) ).start()


if __name__ == '__main__':
    #Thread(target=server_program,daemon=True).start()
    server_program()
