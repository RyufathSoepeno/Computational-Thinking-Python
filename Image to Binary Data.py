import mysql.connector

# Connect to the database
conn = mysql.connector.connect(user='username', password='password', host='hostname', database='database')
cursor = conn.cursor()

# Function to convert image file to binary
def convert_to_binary(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

# Insert data into the table
insert_query = """
INSERT INTO Daftar_Mobil (Nama, Jenis, Tipe, Vendor, Kontrak_Pemelihara, Image)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Data to insert
data = [
    ('Toyota Camry', 'Dinas', 'Sedan', 'Toyota', 'Auto Maintain Inc', convert_to_binary('image1.jpg')),
    ('Toyota Camry', 'Dinas', 'Sedan', 'Toyota', 'Auto Maintain Inc', convert_to_binary('image1.jpg')),
    ('Toyota Camry', 'Dinas', 'Sedan', 'Toyota', 'Auto Maintain Inc', convert_to_binary('image1.jpg')),
    ('Honda Accord', 'Sewa', 'Sedan', 'Honda', 'ServicePro', convert_to_binary('image2.jpg')),
    ('Mitsubishi Pajero', 'Dinas', 'SUV', 'Mitsubishi', 'CarCare Ltd', convert_to_binary('image3.jpg')),
    ('Suzuki Swift', 'Sewa', 'Hatchback', 'Suzuki', 'SwiftMaintain', convert_to_binary('image4.jpg')),
    ('Nissan Navara', 'Dinas', 'Pickup', 'Nissan', 'MaintainPlus', convert_to_binary('image5.jpg')),
    ('Ford Ranger', 'Sewa', 'Pickup', 'Ford', 'TruckCare', convert_to_binary('image6.jpg'))
]

# Execute the insert query
for record in data:
    cursor.execute(insert_query, record)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()
