from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def update_danhmuc(danhmuc_id, ten_danhmuc=None, mo_ta=None, trang_thai=None):
    """Hàm cập nhật thông tin danh mục theo ID."""
    connection = connect_mysql()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        # Danh sách các cột cần cập nhật (chỉ cập nhật nếu có giá trị mới)
        fields = []
        values = []

        if ten_danhmuc is not None:
            fields.append("ten_danhmuc = %s")
            values.append(ten_danhmuc)

        if mo_ta is not None:
            fields.append("mo_ta = %s")
            values.append(mo_ta)

        if trang_thai is not None:
            fields.append("trang_thai = %s")
            values.append(trang_thai)

        if not fields:
            print("⚠️ Không có dữ liệu nào để cập nhật!")
            return

        # Thêm ID vào cuối danh sách giá trị
        values.append(danhmuc_id)

        sql = f"UPDATE danhmuc SET {', '.join(fields)} WHERE id = %s"
        cursor.execute(sql, tuple(values))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục ID = {danhmuc_id}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {danhmuc_id}")
    except Error as e:
        print(f"❌ Lỗi khi cập nhật danh mục: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()