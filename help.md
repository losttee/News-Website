
# Khám phá Django
- Link Document 4.2: https://docs.djangoproject.com/en/4.2/
- Xem version Django: django-admin startproject mysite
- Tạo project mới: django-admin startproject mysite
- Chạy server: python manage.py runserver
- Đổi port: python manage.py runserver 6969
- Tạo app mới: python manage.py startapp polls
- Tạo mới, áp dụng sự thay đổi cho cơ sở dữ liệu: python manage.py migrate
- Tạo user mới: python manage.py createsuperuser
# Áp dụng MySQL
- Tạo database mới tại phpmyadmin
- Config database tại settings.py
- Chạy lệnh python manage.py migrate
# Xây dựng quản lý Category - Thêm Sửa Xóa Đọc - CRUD
- Tạo Category, khai báo các trường tại models.py
- Khai báo app news tại INSTALLED_APP trong settings.py
- python manage.py makemigrations news
- python manage.py migrate
- Thiết lập phần hiển thị cho Category tại admin.py
- Tạo slug từ động từ name
- Tạo đường dẫn static file cho project
- Chạy file Javascript tại trang Admin Django
- Filter: Status, Is Homepage, Layout
- Search: Name
# Xây dựng quản lý Article - Thêm Sửa Xóa Đọc - CRUD
- Link Editor Content: https://pypi.org/project/django-tinymce
- Upload path: https://www.geeksforgeeks.org/python-uploading-images-in-django
- Random name image: https://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django
- Delete image: https://stackoverflow.com/questions/2878490/how-to-delete-old-image-when-update-imagefield

# Xây dựng quản lý Feed - Thêm Sửa Xóa Đọc - CRUD

# Nhúng và tối ưu giao diện cho backend
- Tải và giải nén giao diện template_news tại phần mã nguồn của video
- Xây dựng các thành phần dùng chung (hạn chế lặp lại các thành phần HTML)
- Tạo layout và dùng block content
- Xây dựng các layout con (multi layout)

# Xây dựng trang hiển thị bài viết của mỗi Category
- Dùng get_object_or_404 để tìm dữ liệu trong database (trả về lỗi 404 khi không tìm thấy).
- Lọc bài viết theo category, status và publish_date (filter).
- Sắp xếp bài viết mới nhất trước (order).
- Phân trang bằng Paginator.
- Render html và truyền ra biến dữ liệu để sử dụng tại template.
- Sử dụng các cú pháp đổ dữ liệu, thực hiện câu lệnh if else for tại template django.
- Hàm format ngày tháng, rút gọn nội dung bài viết, đổ html (date, truncatechars, safe).

# Xây dựng trang hiển thị nội dung bài viết
- Loại bỏ bài viết hiện tại trong bài viết liên quan bằng exclude.
- Định nghĩa hàm get_absolute_url, tối ưu việc thay thế đường dẫn.

# Xây dựng trang chủ cho trang tin tức
- Dùng hàm slice để giới hạn lượng bài viết được đổ ra tại django template.

# Xây dựng chức năng tìm kiếm và trang hiển thị kết quả
- Tự tạo 1 template tag sử dụng tại django template.
- Một số lookup dùng để tìm kiếm:
1. contains: Tìm kiếm các giá trị có chứa một chuỗi con cụ thể.
2. icontains: Tìm kiếm các giá trị có chứa một chuỗi con cụ thể (không phân biệt chữ hoa/chữ thường).
3. regex: Tìm kiếm các giá trị phù hợp với một biểu thức chính quy cụ thể.
4. iregex: Tìm kiếm các giá trị phù hợp với một biểu thức chính quy cụ thể (không phân biệt chữ hoa/chữ thường).

# Xây dựng trang tin tức tổng hợp từ nguồn cấp bên ngoài
- Lấy và chuyển dữ liệu rss sang json để xử lý
- Cách ghi json ra 1 file, xử lý trường hợp bị mã hóa nội dung
- Sử dụng Beautiful Soup lấy src image

# Xây dựng các context khởi chạy mặc định
- Category: Menu, Sidebar
- Feed: Menu, Sidebar
- Bài viết gần đây: Sidebar
- Bài viết ngẫu nhiên: Footer

# Xây dựng chức năng hiển thị giá vàng, giá coin
- Link Document API: http://apiforlearning.zendvn.com
- Get Coin: http://apiforlearning.zendvn.com/api/get-coin
- Get Gold: http://apiforlearning.zendvn.com/api/get-gold

# Các câu lệnh thường dùng
- python manage.py runserver
- python manage.py makemigrations
- python manage.py migrate


