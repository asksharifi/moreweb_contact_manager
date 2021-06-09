import pymysql


def connectnow():
    global cn,cr
    host = "localhost"
    user = "root"
    password = "amir9628."
    database = "contact_m"
    try:
        cn = pymysql.connect(host=host, user=user,
                             password=password, db=database)
        cr = cn.cursor()
        print(f"Connection Established Succesfully\nIP : 127.0.0.1 (localhost)\nuser : {user}\nPassword : *********\nMySQL Database\nDatabase : {database}")
    except:
        print("can't connect on LocalHost")


connectnow()
