import sqlite3

def to_create(date):
    global cursor, conn
    conn = sqlite3.connect('request.db')

    cursor = conn.cursor()

    cursor.execute(f'''CREATE TABLE IF NOT EXSIST 
                {date}(who text, breakfast integer,lunch integer, dinner integer )''')
    
def to_write(date,time,number,name):
    to_create(date)
    cursor.execute(f''' INSERT INTO {date} (who, {time}) VALUES ({name},{number})''')
    conn.commit()
    conn.close()
