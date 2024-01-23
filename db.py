import psycopg2
from psycopg2 import sql
import os



class Operations:
    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = os.environ['host']
        self.port = os.environ['port']
        self.connection = None
    def connect(self):
        try:
            connection_string = f"dbname={self.dbname} user={self.user} password={self.password} host={self.host} port={self.port}"
            connection = psycopg2.connect(connection_string)
            print("Connected to the database!")
            self.connection=connection
            return connection
        except Exception as e:
            print(f"Error: {e}")
    def list_tables(self):
        connection=self.connection
        cursor = connection.cursor()
        query = sql.SQL("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = %s
            """)
        try:
            parameters = ('public',)
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            tables=[]
            for row in results:
                # print(row[0]) 
                tables.append(row[0])
            query = sql.SQL("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = %s
            AND table_name = %s;
        """)
            schema_data={}
            for table in tables:
                parameters = ('public', table)

                # Execute the query
                cursor.execute(query, parameters)

                # Fetch and print the results
                results = cursor.fetchall()
                columns={}
                for row in results:
                    # print(f"Column Name: {row[0]}, Data Type: {row[1]}")
                    columns[row[0]] = row[1]
                schema_data[table] = columns

            print(schema_data)
            return schema_data
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
    def search_table(self ,table_name):
        connection = self.connection
        cursor = connection.cursor()
        query = sql.SQL(f"""
                 SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = %s
            AND table_name = %s;
            """)
        try:
            parameters = ('public',table_name)
            cursor.execute(query, parameters)
            results = cursor.fetchall()
          
            columns_dict={}
            for row in results:
                columns_dict[row[0]]=row[1]
            print(columns_dict)
            return columns_dict
        except Exception as e:
            print(f"Error: {e}")
       
    
    
    
    
# if __name__ == "__main__":
#     db_instance = Operations(dbname=dbname, user=user, password=password)

#     try:
#         with db_instance.connect() as connection:
#             db_instance.list_tables()
#             # db_instance.search_table('tab1')

#     except Exception as e:
#         print(f"Error: {e}")