import sqlite3 as sl
con = sl.connect('clients.db')

# with con:
#     con.execute("""
#         CREATE TABLE CLIENTS(
#                 client_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 ip STRING NOT NULL,
#                 port INTEGER NOT NULL
                
#         );
# """)
        

# client_file_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, -- to be added
# client_id INTEGER NOT NULL,
with con:
    con.execute("""

         CREATE TABLE CLIENT_FILES(
                
                
                ip STRING NOT NULL,
                port INTEGER NOT NULL,
                files STRING NOT NULL
                
        );    
        
""")