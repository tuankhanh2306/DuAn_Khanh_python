from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def get_all_danhmuc():
    """Hàm lấy danh sách tất cả danh mục trong bảng danhmuc."""
    connection = connect_mysql()
    if connection is None:
        return []

    danh_sach = []
    try:
        cursor = connection.cursor(dictionary=True)  # dictionary=True để trả về dạng dict
        sql = "SELECT id, ten_danhmuc, mo_ta, trang_thai FROM danhmuc"
        cursor.execute(sql)
        danh_sach = cursor.fetchall()

        print("📋 Danh sách danh mục:")
        for row in danh_sach:
            print(f"ID: {row['id']} | Tên: {row['ten_danhmuc']} | Trạng thái: {row['trang_thai']}")

        return danh_sach
    except Error as e:
        print(f"❌ Lỗi khi lấy danh sách danh mục: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()