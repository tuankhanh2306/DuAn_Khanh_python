import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Hàm kết nối MySQL và trả về đối tượng connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',       # địa chỉ máy chủ MySQL
            user='root',            # tên đăng nhập
            password='',      # mật khẩu
            database='qlthuocankhang'  # tên CSDL bạn muốn kết nối
        )
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection
    except Error as e:
        print(f"❌ Lỗi khi kết nối MySQL: {e}")
        return None
