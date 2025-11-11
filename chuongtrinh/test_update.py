from common.updatedanhmuc import update_danhmuc

while True:
    danhmuc_id=input("Nhập mã danh mục")
    ten_danhmuc=input("Nhập vào tên danh mục")
    mo_ta=input("Nhập vào mô tả")
    update_danhmuc(danhmuc_id,ten_danhmuc, mo_ta)
    con=input("Tiếp tục Y, Thoát bấm kí tự bất kì")
    if con != "Y":
        break