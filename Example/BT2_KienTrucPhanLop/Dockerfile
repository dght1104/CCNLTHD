# Sử dụng Python 3.12
FROM python:3.12

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép toàn bộ mã nguồn vào container
COPY . /app/

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Chạy migration (nếu cần)
RUN python manage.py migrate

# Mở cổng 8000
EXPOSE 8000

# Lệnh chạy server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]