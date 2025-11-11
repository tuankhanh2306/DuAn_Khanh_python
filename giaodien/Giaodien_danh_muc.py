# ====== GIAO DIỆN TKINTER ======
from common.deletedanhmuc import delete_danhmuc
from common.getdanhmuc import get_all_danhmuc
from common.insertdanhmuc import insert_danhmuc
from common.updatedanhmuc import update_danhmuc
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
def on_select(event):
    selected = tree.focus()
    if not selected:
        return
    data = tree.item(selected)["values"]
    entry_ten.delete(0, tk.END)
    entry_ten.insert(0, data[1])
    entry_mota.delete(0, tk.END)
    entry_mota.insert(0, data[2])
    entry_trangthai.delete(0, tk.END)
    entry_trangthai.insert(0, data[3])


root = tk.Tk()
root.title("Quản lý Danh Mục Sản Phẩm")
root.geometry("700x500")

# Frame nhập liệu
frame_input = ttk.LabelFrame(root, text="Thông tin danh mục")
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_ten = tk.Entry(frame_input, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_mota = tk.Entry(frame_input, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Trạng thái (1=Hiện, 0=Ẩn):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_trangthai = tk.Entry(frame_input, width=10)
entry_trangthai.insert(0, "1")
entry_trangthai.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# ====== BẢNG HIỂN THỊ ======
frame_table = ttk.LabelFrame(root, text="Danh sách danh mục")
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

tree = ttk.Treeview(frame_table, columns=("id", "ten", "mota", "trangthai"), show="headings")
tree.heading("id", text="ID")
tree.heading("ten", text="Tên danh mục")
tree.heading("mota", text="Mô tả")
tree.heading("trangthai", text="Trạng thái")
tree.pack(fill="both", expand=True)

def load_data():
    for i in tree.get_children():
        tree.delete(i)
    for row in get_all_danhmuc():
        tree.insert("", tk.END, values=(row["id"], row["ten_danhmuc"], row["mo_ta"], row["trang_thai"]))

def clear_inputs():
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)
    entry_trangthai.delete(0, tk.END)
    entry_trangthai.insert(0, "1")

def on_add():
    ten = entry_ten.get()
    mota = entry_mota.get()
    trangthai = entry_trangthai.get()
    if not ten:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return
    insert_danhmuc(ten, mota, trangthai)
    load_data()
    clear_inputs()
    messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")

def on_update():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để cập nhật!")
        return
    data = tree.item(selected)["values"]
    danh_muc_id = data[0]
    update_danhmuc(danh_muc_id, entry_ten.get(), entry_mota.get(), entry_trangthai.get())
    load_data()
    messagebox.showinfo("Thành công", "Cập nhật danh mục thành công!")

def on_delete():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để xóa!")
        return
    data = tree.item(selected)["values"]
    danh_muc_id = data[0]
    if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa danh mục ID {danh_muc_id}?"):
        delete_danhmuc(danh_muc_id)
        load_data()
        clear_inputs()
        messagebox.showinfo("Thành công", "Đã xóa danh mục!")

def on_select(event):
    selected = tree.focus()
    if not selected:
        return
    data = tree.item(selected)["values"]
    entry_ten.delete(0, tk.END)
    entry_ten.insert(0, data[1])
    entry_mota.delete(0, tk.END)
    entry_mota.insert(0, data[2])
    entry_trangthai.delete(0, tk.END)
    entry_trangthai.insert(0, data[3])

tree.bind("<<TreeviewSelect>>", on_select)

# ====== NÚT CHỨC NĂNG ======
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Thêm", width=10, command=on_add, bg="#28a745", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Cập nhật", width=10, command=on_update, bg="#007bff", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Xóa", width=10, command=on_delete, bg="#dc3545", fg="white").grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="Làm mới", width=10, command=load_data).grid(row=0, column=3, padx=5)

# ====== KHỞI TẠO DỮ LIỆU ======
load_data()

root.mainloop()