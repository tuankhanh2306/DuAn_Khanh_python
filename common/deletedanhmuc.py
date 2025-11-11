from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def delete_danhmuc(danhmuc_id):
    """Hàm xóa danh mục theo ID."""
    connection = connect_mysql()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(sql, (danhmuc_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có ID = {danhmuc_id}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {danhmuc_id}")
    except Error as e:
        print(f"❌ Lỗi khi xóa danh mục: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()