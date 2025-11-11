-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 02:38 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `id` int(11) NOT NULL,
  `ten_danhmuc` varchar(100) NOT NULL,
  `mo_ta` text DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`id`, `ten_danhmuc`, `mo_ta`, `trang_thai`) VALUES
(1, 'Hot Sale', 'giảm giá cực sốc', 1),
(2, 'Thuốc Long Châu', 'hàng chất lượng', 1),
(3, 'Mỹ phẩm ', 'phái nữ làm đẹp', 1),
(4, 'Thiết bị, dụng cụ y tế', 'đã kiểm định của Bộ Y Tế', 1),
(5, 'Dược mỹ phẩm', NULL, 1),
(6, 'Chăm sóc cá nhân', NULL, 1),
(7, 'Chăm sóc trẻ em', NULL, 1),
(10, 'Quần áo ', 'may sẵn sang đẹp', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `id` int(11) NOT NULL,
  `ten_sanpham` varchar(200) NOT NULL,
  `mo_ta` text DEFAULT NULL,
  `gia_goc` decimal(12,0) DEFAULT NULL,
  `gia_giam` decimal(12,0) DEFAULT NULL,
  `phan_tram_giam` int(11) DEFAULT NULL,
  `dung_tich_hoac_khoi_luong` varchar(50) DEFAULT NULL,
  `don_vi` varchar(20) DEFAULT NULL,
  `hinh_anh` varchar(255) DEFAULT NULL,
  `danhmuc_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`id`, `ten_sanpham`, `mo_ta`, `gia_goc`, `gia_giam`, `phan_tram_giam`, `dung_tich_hoac_khoi_luong`, `don_vi`, `hinh_anh`, `danhmuc_id`) VALUES
(1, 'Nước muối Vietrue sát khuẩn, súc miệng', 'Dung tích 500ml', 7000, 4900, 30, '500ml', 'chai', 'vietrue500.jpg', 3),
(2, 'Thực phẩm dinh dưỡng Y Học Ensure Gold', 'Lon 800g', 932000, 845000, 9, '800g', 'lon', 'ensuregold800.jpg', 3),
(3, 'Sữa bột Anlene Gold hương Vani', 'Lon 800g, dành cho người trên 40 tuổi', 555000, 480000, 13, '800g', 'lon', 'anlenegold800.jpg', 3);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`id`),
  ADD KEY `danhmuc_id` (`danhmuc_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`danhmuc_id`) REFERENCES `danhmuc` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
