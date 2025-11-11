from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(ten_danhmuc, mo_ta=None, trang_thai=1):
    """Hàm thêm một danh mục mới vào bảng danhmuc."""
    connection = connect_mysql()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        sql = """
            INSERT INTO danhmuc (ten_danhmuc, mo_ta, trang_thai)
            VALUES (%s, %s, %s)
        """
        values = (ten_danhmuc, mo_ta, trang_thai)
        cursor.execute(sql, values)
        connection.commit()
        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
    except Error as e:
        print(f"❌ Lỗi khi thêm danh mục: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()