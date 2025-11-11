from common.insertdanhmuc import insert_danhmuc
while True:
    ten_danhmuc=input("Nhập vào tên danh mục")
    mo_ta=input("Nhập vào mô tả")
    insert_danhmuc(ten_danhmuc, mo_ta)
    con=input("Tiếp tục Y, Thoát bấm kí tự bất kì")
    if con != "Y":
        break