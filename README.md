# Phần Mềm Xử Lý Ảnh

Ứng dụng máy tính mạnh mẽ để xử lý hình ảnh và chú thích dựa trên lưới, được xây dựng bằng Python và PySide6.

## Tính Năng

- **Xử Lý Ảnh**
  - Mở và lưu ảnh với nhiều định dạng (PNG, JPEG, BMP)
  - Hỗ trợ kéo thả
  - Xem trước ảnh trước khi lưu

- **Hệ Thống Lưới**
  - Lớp phủ lưới tương tác
  - Tùy chỉnh kích thước lưới
  - Chú thích ô
  - Điều khiển di chuyển và thay đổi kích thước lưới

- **Điều Khiển Lưới**
  - Phím mũi tên: Di chuyển lưới (↑, ↓, ←, →)
  - Giữ Shift + Phím mũi tên: Điều khiển di chuyển chính xác
  - W/S: Điều chỉnh chiều cao ô (Shift + W/S để giảm)
  - A/D: Điều chỉnh chiều rộng ô (Shift + A/D để giảm)
  - Nhấp vào ô để thêm chú thích

- **Công Cụ Xử Lý Ảnh**
  - Xoay
  - Lật
  - Cắt
  - Bộ lọc
  - Chế độ tự động cho xử lý tự động

## Cài Đặt

1. Tải mã nguồn:
```bash
git clone https://github.com/ThangStar/Image-Mask-Studio
cd Image-Mask-Studio
pyside6-uic gui/qt/main.ui -o gui/qt/build/main_ui.py 
pyside6-uic gui/qt/preview_image.ui -o gui/qt/build/preview_image_ui.py
```