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
│   └── supplierController.py # Logic xử lý nhà cung cấp
├── model/
│   ├── device.py             # Model dữ liệu thiết bị
│   ├── deviceRoutes.py       # Thao tác cơ sở dữ liệu thiết bị
│   ├── category.py           # Model dữ liệu danh mục
│   └── categoryRoutes.py     # Thao tác cơ sở dữ liệu danh mục
|   ├── supplier.py          # Model dữ liệu nhà cung cấp
│   └── supplierRoutes.py    # Thao tác cơ sở dữ liệu nhà cung cấp
└── view/
    └── view.py               # Giao diện người dùng
```


1. Thiết lập cơ sở dữ liệu MySQL
   - Tạo cơ sở dữ liệu MySQL tên `tech_inventory_db`
   - Tạo các bảng cần thiết:

   ```sql
   CREATE DATABASE tech_inventory_db;
   USE tech_inventory_db;

   CREATE TABLE `category` (
      `category_id` int(11) NOT NULL,
      `name` varchar(255) NOT NULL,
      `description` text DEFAULT NULL
    )

   CREATE TABLE `device` (
      `device_id` int(11) NOT NULL,
      `name` varchar(255) NOT NULL,
      `category_id` int(11) DEFAULT NULL,
      `supplier_id` int(11) DEFAULT NULL,
      `quantity` int(11) NOT NULL,
      `price` decimal(12,2) NOT NULL,
      `manufacturer` varchar(255) DEFAULT NULL,
      `description` text DEFAULT NULL,
      `status` varchar(50) NOT NULL DEFAULT 'Available',
      `created_at` datetime DEFAULT current_timestamp(),
      `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
    )

   CREATE TABLE `supplier` (
      `supplier_id` int(11) NOT NULL,
      `name` varchar(255) NOT NULL,
      `contact_person` varchar(255) DEFAULT NULL,
      `phone` varchar(20) DEFAULT NULL,
      `email` varchar(255) DEFAULT NULL,
      `address` text DEFAULT NULL
    )

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
   - Thêm thiết bị: Điền form và nhấn "Add"
   - Cập nhật thiết bị: Chọn thiết bị từ danh sách, sửa form và nhấn "Update"
   - Xóa thiết bị: Chọn thiết bị và nhấn "Delete"
   - Tìm kiếm: Nhập tên thiết bị vào ô search và nhấn "Search"
   - Làm mới: Nhấn "Refresh" để tải lại danh sách

<img width="1152" height="708" alt="image" src="https://github.com/user-attachments/assets/3ca6db6d-bef5-45b4-a0d1-5ea89a9842e9" />

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
