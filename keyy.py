import requests
import sys
import time
import json
import os
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor


KEY_FILE = "saved_keys.json"  # File lưu key đã nhập


def get_ip_address():
    """Lấy địa chỉ IP của thiết bị"""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except requests.ConnectionError:
        print("\033[1;91mKhông thể lấy địa chỉ IP! Kiểm tra kết nối mạng.")
        sys.exit()


def get_default_key_from_github():
    """Lấy key mặc định từ GitHub"""
    url = "https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/key.txt"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except requests.ConnectionError:
        pass#print("\033[1;91mKhông thể lấy key từ GitHub! Kiểm tra kết nối mạng.")
    return None


def get_shortened_link_phu(url):
    """Rút gọn URL bằng Yeumoney"""
    try:
        token = "1f06c470cc45a0d11ef440cb959c716466487b6b46c78b099fe7d1804e573235"
        api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=json&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.json().get('shortenedUrl')
    except requests.ConnectionError:
        print("\033[1;91mLỗi khi kết nối đến Yeumoney! Kiểm tra mạng.")
    return None


def generate_key_and_url(ip_address):
    """Tạo key Yeumoney theo ngày + IP"""
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'Mle{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://mlevip.blogspot.com/2025/02/mlevip.html?ma={key}'
    return url, key, expiration_date


def save_key(key, expiration_date):
    """Lưu key vào file cùng với ngày hết hạn"""
    data = {"key": key, "expiration_date": expiration_date.isoformat()}
    with open(KEY_FILE, "w") as file:
        json.dump(data, file)


def load_saved_key():
    """Đọc key đã lưu trong file và kiểm tra hạn sử dụng"""
    if not os.path.exists(KEY_FILE):
        return None

    try:
        with open(KEY_FILE, "r") as file:
            data = json.load(file)
            expiration_date = datetime.fromisoformat(data["expiration_date"])

            if expiration_date > datetime.now():
                return data["key"]  # Key còn hạn, trả về key
            else:
                print("\033[1;91mKey đã hết hạn! Vui lòng nhập key mới.")
                return None
    except (json.JSONDecodeError, KeyError):
        return None


def main():
    ip_address = get_ip_address()
    saved_key = load_saved_key()

    if saved_key:
        print("\033[1;92mKey hợp lệ! Mời bạn dùng tool.")
        time.sleep(2)
        return  # Nếu key còn hạn, thoát main() luôn

    default_key = get_default_key_from_github()
    url, key_yeumoney, expiration_date = generate_key_and_url(ip_address)

    with ThreadPoolExecutor(max_workers=2) as executor:
        yeumoney_future = executor.submit(get_shortened_link_phu, url)
        link_key_yeumoney = yeumoney_future.result()

        print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập Key Để Dùng Tool")

        if link_key_yeumoney:
            print(f"\033[1;35mVượt link để lấy key Yeumoney: \033[1;36m{link_key_yeumoney}")

        while True:
            try:
                keynhap = input("\033[1;33mNhập Key: \033[1;32m").strip()
                if keynhap in [key_yeumoney, default_key]:
                    print("\033[1;92mKey đúng! Mời bạn dùng tool.")
                    save_key(keynhap, expiration_date)  # Lưu key lại để dùng sau
                    time.sleep(2)
                    return
                else:
                    print("\033[1;91mKey sai! Vui lòng nhập lại hoặc kiểm tra GitHub/Yeumoney.")
            except KeyboardInterrupt:
                print("\n\033[1;91mThoát tool!")
                sys.exit()


if __name__ == '__main__':
    main()

while True:
    try:
        response = requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/menuu.py', timeout=5)
        exec(response.text)
    except requests.ConnectionError:
        print("\033[1;91mMất kết nối! Tool sẽ tự động thoát.")
        sys.exit()
    except KeyboardInterrupt:
        print("\n\033[1;91mCảm ơn bạn đã dùng Tool!")
        sys.exit()
