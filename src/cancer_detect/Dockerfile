# Sử dụng image Python chính thức
FROM python:3.10

# Cài thư viện hệ thống cần thiết cho OpenCV và pyodbc
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Copy mã nguồn vào container
COPY . .

# Cài thư viện Python
RUN pip install --no-cache-dir -r requirements.txt

# Mở port Django
EXPOSE 8001

# Lệnh chạy Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
