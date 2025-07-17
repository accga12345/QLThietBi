Hệ Thống Quản Lý Thiết Bị

Các tính năng bao gồm
- Quản lý thiết bị: Thêm, sửa, xóa và tìm kiếm thiết bị
- Tìm kiếm: Tìm kiếm thiết bị theo tên
- Xác thực dữ liệu: Ngăn chặn tên thiết bị trùng lặp
- Giao diện trực quan: form nhập liệu và bảng dữ liệu

```
QLThietBi/
├── main.py                 # Điểm khởi chạy ứng dụng
├── connect_db.py          # Cấu hình kết nối cơ sở dữ liệu
├── controller/
│   ├── deviceController.py    # Logic xử lý thiết bị
│   └── categoryController.py  # Logic xử lý danh mục
├── model/
│   ├── device.py             # Model dữ liệu thiết bị
│   ├── deviceRoutes.py       # Thao tác cơ sở dữ liệu thiết bị
│   ├── category.py           # Model dữ liệu danh mục
│   └── categoryRoutes.py     # Thao tác cơ sở dữ liệu danh mục
└── view/
    └── view.py               # Giao diện người dùng
```


1. Thiết lập cơ sở dữ liệu MySQL
   - Tạo cơ sở dữ liệu MySQL tên `tech_inventory_db`
   - Tạo các bảng cần thiết:

   ```sql
   CREATE DATABASE tech_inventory_db;
   USE tech_inventory_db;

   CREATE TABLE category (
       category_id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       description TEXT
   );

   CREATE TABLE device (
       device_id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL UNIQUE,
       category_id INT,
       quantity INT NOT NULL,
       price DECIMAL(10,2) NOT NULL,
       manufacturer VARCHAR(255),
       description TEXT,
       status VARCHAR(50),
       FOREIGN KEY (category_id) REFERENCES category(category_id)
   );
   ```

2. Cấu hình kết nối cơ sở dữ liệu
   Cập nhật thông tin đăng nhập database trong file `connect_db.py`:
   ```python
   conn = mysql.connector.connect(
       host='localhost',
       user='root',
       password='mat_khau_cua_ban',  # Cập nhật mật khẩu MySQL của bạn
       database='tech_inventory_db'
   )
   ```

3. Cách Sử Dụng

3.1. Sử dụng giao diện
   - **Thêm thiết bị**: Điền form và nhấn "Add"
   - **Cập nhật thiết bị**: Chọn thiết bị từ danh sách, sửa form và nhấn "Update"
   - **Xóa thiết bị**: Chọn thiết bị và nhấn "Delete"
   - **Tìm kiếm**: Nhập tên thiết bị vào ô search và nhấn "Search"
   - **Làm mới**: Nhấn "Refresh" để tải lại danh sách

3.2. Cấu Trúc Cơ Sở Dữ Liệu

Bảng `category`
- `category_id`: Khóa chính (INT, AUTO_INCREMENT)
- `name`: Tên danh mục (VARCHAR(255))
- `description`: Mô tả danh mục (TEXT)

Bảng `device`
- `device_id`: Khóa chính (INT, AUTO_INCREMENT)
- `name`: Tên thiết bị (VARCHAR(255), UNIQUE)
- `category_id`: Khóa ngoại liên kết với bảng category (INT)
- `quantity`: Số lượng (INT)
- `price`: Giá (DECIMAL(10,2))
- `manufacturer`: Nhà sản xuất (VARCHAR(255))
- `description`: Mô tả (TEXT)
- `status`: Trạng thái (VARCHAR(50))

4. Các Tính Năng Chính

4.1. Quản lý thiết bị
- Thêm thiết bị mới với đầy đủ thông tin
- Cập nhật thông tin thiết bị đã có
- Xóa thiết bị khỏi hệ thống
- Xem danh sách tất cả thiết bị

4.2. Tìm kiếm và lọc
- Tìm kiếm thiết bị theo tên
- Hiển thị kết quả tìm kiếm real-time

4.3. Xác thực dữ liệu
- Kiểm tra tên thiết bị không trùng lặp
- Xác thực định dạng dữ liệu đầu vào

4.4. Giao diện 
- Form nhập liệu 
- Bảng hiển thị dữ liệu có thể sắp xếp
- Thông báo lỗi và thành công

5. Xử Lý Lỗi
Ứng dụng có các cơ chế xử lý lỗi:
- Kiểm tra kết nối cơ sở dữ liệu
- Xác thực dữ liệu đầu vào
- Thông báo lỗi cho người dùng

Ghi Chú
- Đảm bảo MySQL server đang chạy trước khi khởi động ứng dụng
- Kiểm tra thông tin kết nối database trong file `connect_db.py`
