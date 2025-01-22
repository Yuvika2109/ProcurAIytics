import mysql.connector
import csv


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yuvika@1234",
    database="tsdpl"
)

cursor = mydb.cursor()


cursor.execute("DROP TABLE IF EXISTS details")


create_table_sql = """
CREATE TABLE details (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Add an auto-increment primary key
    doc_no BIGINT,  -- Allow doc_no to have duplicates
    material VARCHAR(200),
    text VARCHAR(200),
    location VARCHAR(200),
    quantity INT,
    price INT,
    validity VARCHAR(200),
    doc_type VARCHAR(100),
    grp INT,
    supplier VARCHAR(100),
    net_value INT
);
"""
cursor.execute(create_table_sql)


filename = "cleaned.csv"
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  
    
   
    for row in csvreader:
        doc_no = int(row[0])
        material = row[1]
        text = row[2]
        location = row[3]
        quantity = int(row[4])
        price = int(row[5])
        validity = row[6]
        doc_type = row[7]
        grp = int(row[8])
        supplier = row[9]
        net_value = int(row[10])
        
     
        insert_sql = """
        INSERT INTO details (doc_no, material, text, location, quantity, price, validity, doc_type, grp, supplier, net_value)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        val = (doc_no, material, text, location, quantity, price, validity, doc_type, grp, supplier, net_value)
        
        cursor.execute(insert_sql, val)


mydb.commit()
cursor.close()
mydb.close()





