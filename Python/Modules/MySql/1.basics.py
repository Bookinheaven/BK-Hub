import mysql.connector as Connector

connection = Connector.connect(
    host='localhost', 
    user='root', 
    passwd='tanvik37')

mycur = connection.cursor()

# mycur.execute("create database BurnKnuckle")
# mycur.execute("show databases")
# for x in mycur:
#     print(x)
mycur.execute("use burnknuckle")
# mycur.execute("create table apper (user_id int(10), user_name varchar(30), date_of_birth date)")
# mycur.execute("show tables")
# mycur.execute("desc apper")

# mycur.execute('insert into apper values(123, "BK", "2005/03/01")')
# mycur.execute("select * from apper")
# connection.commit()

# mycur.execute('update apper set user_id=124 where user_name="BK"')
# connection.commit()

# mycur.execute('delete from apper where user_name = "K"')
# connection.commit()

# command = 'insert into apper values(%s, %s, %s)'
# list_commands = [(145, "Hello", "2005/4/1"), (115, "Hey", "2005/5/1"), (105, "Hy", "2009/5/1")]
# mycur.executemany(command, list_commands)
# connection.commit()

#mycur.fetchall()
#mycur.fetchmany(size)
#mycur.fetchone()

mycur.execute("select * from apper")
for x in mycur:
    print(x)
print("Row Count: ", mycur.rowcount)
connection.close()