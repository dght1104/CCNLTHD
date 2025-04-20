import pyodbc

# Kết nối đến SQL Server
try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=127.0.0.1;'
        'PORT=1433;'
        'DATABASE=Bone_tumor;'
        'UID=sa;'
        'PWD=1104'
    )
    print("Kết nối thành công")
    conn.close()
except Exception as e:
    print(f"Lỗi kết nối: {e}")