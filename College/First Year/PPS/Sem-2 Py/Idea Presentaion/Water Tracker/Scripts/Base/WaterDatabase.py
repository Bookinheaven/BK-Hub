import psycopg2
import logging
class Database:
    def __init__(self):
        self.connection = None
        self.logger = self.Logger_setup()
        self.__connection_check()
    def Logger_setup(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s | %(message)s', datefmt='%d-%m-%Y | %I:%M:%S %p')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler('logfile.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
    def __connection_check(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                database="aquaintake",
                user="burn",          
                password="i3urnknuckle#124",
                port=5432  
            )
            # self.logger.info("Database Connected Successfully!")
        except psycopg2.Error as e:
            self.logger.error(f"Error connecting to the database: {e}")
            raise
        if self.connection == None:
            try:
                self.connection=  psycopg2.connect("postgresql://aquaintake_owner:OXnERG1HU2Jv@ep-wispy-boat-a2c8z4i7.eu-central-1.aws.neon.tech/aquaintake?sslmode=require")
                    # self.logger.info("Database Connected Successfully!")
            except psycopg2.OperationalError as e:
                self.logger.error(f"Error connecting to the database: {e}")
                raise
            except psycopg2.Error as e:
                self.logger.error(f"Error: {e}")
                raise
            except Exception as e:
                self.logger.error(f"Unexpected error: {e}")
                raise

    @staticmethod
    def table_exists(cursor, table_name):
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table_name,))
        return cursor.fetchone()[0]

    def create_userstats(self):
        try:
            with self.connection.cursor() as cursor:
                if not self.table_exists(cursor, 'userstats') and self.table_exists(cursor, 'userdata'):
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS userstats (
                            userid VARCHAR(20) PRIMARY KEY NOT NULL,
                            dailyintakegoal FLOAT NOT NULL DEFAULT 0,
                            currentwaterintake FLOAT NOT NULL DEFAULT 0,
                            dailypoints INT DEFAULT 100,
                            currentpoints INT DEFAULT 0,
                            waterintakehistory JSON,
                            lastweightupdate TIMESTAMP,
                            lastheightupdate TIMESTAMP,
                            lastprofileupdate TIMESTAMP,
                            lastresettime TIMESTAMP,
                            FOREIGN KEY (userid) REFERENCES userdata(userid)
                        );
                    """)
                    cursor.execute("SET datestyle = mdy;")
                    print("Created Table 'userstats' Successfully!")
                    self.connection.commit()
        except psycopg2.Error as e:
            self.logger.error(f"Error creating tables: {e}")
            raise
    def create_tables(self):

        try:
            with self.connection.cursor() as cursor:
                if not self.table_exists(cursor, 'userdata'):
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS userdata (   
                            userid VARCHAR(20) PRIMARY KEY NOT NULL,
                            name VARCHAR(50) NOT NULL,
                            username VARCHAR(50) UNIQUE NOT NULL,
                            password VARCHAR(100) NOT NULL,
                            dob DATE NOT NULL,
                            gender VARCHAR(10) NOT NULL,
                            email VARCHAR(100) NOT NULL,
                            activity_level VARCHAR(20) NOT NULL,
                            height INT NOT NULL,
                            weight INT NOT NULL,
                            register_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            level INT DEFAULT 1,
                            experiencepoints INT DEFAULT 0,
                            lastlogin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            verificationcode VARCHAR(10),
                            verificationtime TIMESTAMP,
                            verifiedcode BOOLEAN DEFAULT FALSE,
                            recoveryemail VARCHAR(100),
                            recoverycode VARCHAR(10)
                        );
                    """)
                    self.logger.info("Created Table 'userdata' Successfully!")

                    cursor.execute("SET datestyle = mdy;")
                if not self.table_exists(cursor, 'userstats'):
                    self.create_userstats()
                self.connection.commit()
        except psycopg2.Error as e:
            self.logger.error(f"Error creating tables: {e}")
            raise
    def get_all_values(self, tablename):
        try:
            with self.connection.cursor() as cursor:
                if not self.table_exists(cursor, 'userdata'):
                    self.create_tables()
                cursor.execute(f"SELECT * FROM {tablename}")
                rows = cursor.fetchall()
                data = []
                for row in rows:
                    data.append(row)
                self.connection.commit()
                return data
        except psycopg2.Error as e:
            self.logger.error(f"Error retrieving data: {e}")
            raise

    def get_values(self, tablename, userid: str= None,username: str = None):
        try:
            with self.connection.cursor() as cursor:
                if not self.table_exists(cursor, f'{tablename}'):
                    self.create_tables()
                if userid:
                    cursor.execute(f"SELECT * FROM {tablename} WHERE userid='{userid}';")
                elif username: 
                    cursor.execute(f"SELECT * FROM {tablename} WHERE username='{username}';")
                rows = cursor.fetchall() 
                # print(rows) 
                self.connection.commit()
                return rows 
        except psycopg2.Error as e:
            self.logger.error(f"Error retrieving data: {e}")
            raise

    def update_values(self, tablename, data):
        try: 
            with self.connection.cursor() as cursor:
                if not self.table_exists(cursor, f'{tablename}'):
                    self.create_tables()

                cursor.execute("SELECT EXISTS (SELECT 1 FROM {} WHERE userid = %s)".format(tablename), (data['userid'],))
                data_exists = cursor.fetchone()[0]
                # print(f"data['userid']: {data['userid']}")

                if data_exists:
                    set_query = ', '.join([f"{key} = %s" for key in data.keys()])
                    update_query = f"UPDATE {tablename} SET {set_query} WHERE userid = %s"
                    update_values = list(data.values()) + [data['userid']]
                    # print(f"update_values: {update_values}")
                    cursor.execute(update_query, update_values)
                    self.connection.commit()
                    # print("Data updated successfully.")
                else:
                    self.set_values(tablename, data)
                    # print("Data created successfully.")

        except Exception as e: 
            self.logger.info(f"Update Value Error: {e}")



    def set_values(self, tablename, data):
        try:
            with self.connection.cursor() as cursor:
                if not self.table_exists(cursor, f'{tablename}'):
                    self.create_tables()
                if 'username' in data and data['username']:
                    username_od = data['username']
                    user_id = 'username'
                else:
                    username_od = data['userid']
                    user_id = 'userid'
                # print(username_od)
                
                cursor.execute("SELECT EXISTS (SELECT 1 FROM {} WHERE {} = %s)".format(tablename, user_id) ,(username_od,))

                data_exists = cursor.fetchone()[0]
                
                if data_exists:
                    # print("Data with username '{}' already exists in the '{}' table.".format(username_od, tablename))
                    return False
                else:
                    columns = ', '.join(data.keys())
                    placeholders = ', '.join(['%s'] * len(data))
                    query = f"INSERT INTO {tablename} ({columns}) VALUES ({placeholders})"
                    
                    # if tablename == 'userstats':
                        # for key in ('waterintakehistory','lastweightupdate', 'lastheightupdate', 'lastprofileupdate'):
                    for key, value in data.items():
                        if value == '':
                            data[key] = None
                    cursor.execute(query, tuple(data.values()))
                    self.connection.commit()
                    return True
                    # print("Data added successfully to the '{}' table.".format(tablename))
        except psycopg2.Error as e:
            self.logger.error(f"Error inserting data from database: setdata: {tablename} {e}")

    def close_connection(self):
        try:
            self.connection.close()
            # print("Connection Closed Successfully!")
        except psycopg2.Error as e:
            self.logger.error(f"Error closing the connection: {e}")
            raise


if __name__ == "__main__":
    db = Database()
    # table_name = 'userdata'
    # cursor = db.connection.cursor()
    # cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table_name,))
    # print(cursor.fetchone())
        # data = {'name': 'tanvik sri ram', 'username': 'BrunKnuckles', 'password': 'tanvik123', 'dob': '2/8/24', 'gender': 'Male', 'email': 'tanvik@gmail.com', 'activity_level': 'Low Level', 'weight': '62', 'height': '152', 'register_time': datetime.datetime(2024, 2, 25, 13, 41, 4, 869351)}
    # db.get_values('userdata')
    # db.set_values(tablename='userdata', data=data)
    # db.close_connection()
