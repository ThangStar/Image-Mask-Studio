# Tool Xóa Nền và Thay Số

Tool này cho phép người dùng xóa nền và thay thế số trong vùng được chọn của ảnh. Phù hợp cho việc chỉnh sửa các bảng số liệu hoặc tài liệu có định dạng số.

## Tính năng chính

- 🖱️ Kéo thả để chọn vùng cần xử lý
- 🎯 Tự động căn chỉnh vào ô có sẵn
- 🔄 Xóa nền tự động trong vùng được chọn
- 📝 Nhập số mới để thay thế
- 🔍 Zoom in/out để xử lý chi tiết
- ↔️ Di chuyển ảnh dễ dàng
- ⚡ Xử lý nhanh chóng

## Cách sử dụng

1. **Khởi động tool:**
   ```bash
   python main.py
   ```

2. **Mở ảnh:**
   - Click nút "Open Image" hoặc kéo thả file ảnh vào cửa sổ
   - Hỗ trợ các định dạng: PNG, JPG, JPEG

3. **Xử lý ảnh:**
   - Click và kéo để tạo ô vuông đỏ trong vùng cần xử lý
   - Kéo ô vuông đến vị trí cần thay đổi (sẽ chuyển xanh khi đúng vị trí)
   - Thả chuột để tự động xóa nền và chuẩn bị nhập số mới
   - Nhập số mới vào ô input
   - Nhấn Enter hoặc click "Apply" để hoàn tất

4. **Điều chỉnh view:**
   - Scroll chuột để zoom in/out
   - Giữ phím Space + kéo chuột để di chuyển ảnh
   - Điều chỉnh kích thước ô vuông bằng cách kéo góc phải dưới

## Phím tắt

- `Space + Kéo chuột`: Di chuyển ảnh
- `Ctrl + Z`: Hoàn tác thao tác cuối
- `Ctrl + S`: Lưu ảnh
- `Esc`: Hủy vùng chọn hiện tại

## Yêu cầu hệ thống

- Python 3.7+
- OpenCV
- Tkinter
- NumPy
- Pillow
