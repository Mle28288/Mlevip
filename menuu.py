import os
import requests 
import sys
import time
from tabulate import tabulate
from pystyle import Write
from tabulate import tabulate
from pystyle import Colorate, Colors
from datetime import datetime
from colorama import Fore, Style, init
import sys
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from pystyle import*
from time import sleep

print('__Các thư viện đã được kiểm tra và cài đặt (nếu cần)__')
os.system('cls' if os.name == 'nt' else 'clear')
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\033[35m"
hong = "\033[1;95m"
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"
import os
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\033[1;32m[●] Đang Vào Tool Đợi Xíu ........');time.sleep(0.1)
xoss('\n\033[1;36m[●] kiểm tra sever.......')
xoss('\n\033[1;33m[●] kiểm tra bản update ')
xoss('\n\033[1;34m[●] thành công đang tiến hành vào tool')
def Update():
    exit('\033[1;31m[●] Đang Tiến Hành Vào Tool...... ')
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

# Lmao
thanh_xau=trang+'~'+do+'['+vang+'✔️'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
banner = r"""

                                                                                                                                            
                          ENTER ĐỂ VÀO TOOL                                
"""
Anime.Fade(Center.Center(banner), Colors.blue_to_green, Colorate.Vertical, enter=True)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

if __name__ == "__main__":
    main()
# Mã màu ANSI cho 7 sắc cầu vồng
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định
def banner():
    # Xóa màn hình
    os.system('cls' if os.name == 'nt' else 'clear')

    # Danh sách màu luân phiên
    colors = [Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.BLUE]

    banner_text = '''
            ─────────────────────────────────────────
    🎀✨ Chào mừng bạn đến với Tool ✨🎀
    ─────────────────────────────────────────
    🌸 Chúc bạn một ngày vui vẻ và nhiều may mắn! 🌸
    🐱 Mèo con chúc bạn code không lỗi! 🐱
    ─────────────────────────────────────────
      🛠️ Admin support tool Zalo:  0367742346
                                   0348865758
        Web tải tool và HD:
	 https://mlevip.blogspot.com/2025/02/huong-dan-su-dung-tool-body-font-family.html
      🔗 Chat support: https://zalo.me/g/uaahwq871
      🌐 Web VPN giá rẻ & ID Apple free: timgiare.top ✔️
    ─────────────────────────────────────────
    CopyRight: © KEDO@TOOL
    '''

    # Hiệu ứng nhấp nháy
    for _ in range(5):
        color = colors[_ % len(colors)]
        print(color + banner_text)
        time.sleep(0.3 )
        os.system('cls' if os.name == 'nt' else 'clear')

    # Hiển thị banner lần cuối với màu nổi bật
    print(Fore.LIGHTCYAN_EX + banner_text)
    print(Fore.LIGHTRED_EX + "-"*70)

def LIST():
    banner()

os.system('cls' if os.name == 'nt' else 'clear')
banner()
if __name__ == "__main__":
    main()
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
# Mã màu ANSI cho nhiều màu sắc
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định

def in_dong_khung_cau_vong(text):
    # Tạo khung với màu sắc thay đổi cho mỗi ký tự trong thanh ngang và nội dung
    khung_tren = "┌"
    khung_duoi = "└"
    
    for i in range(len(text) + 2):
        khung_tren += rainbow_colors[i % len(rainbow_colors)] + "─" + reset_color
    khung_tren += "┐"
    
    # Tô màu cho nội dung bên trong
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung = noi_dung + reset_color
    
    dong_duoc_khung = f"{khung_tren}\n{rainbow_colors[6]}│ {noi_dung} │{reset_color}\n{khung_duoi}"
    
    print(dong_duoc_khung)

# Mã màu ANSI cho nhiều màu sắc
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định

def in_mau(text):
    # Tô màu cho nội dung
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung += reset_color
    
    print(noi_dung)
    

# Các dòng được đóng khung 7 sắc cầu vồng
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Auto Golike    \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1] Tool Auto TikTok ADB auto follow,tim...')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.1] Tool Auto Facebook[Vip-PC]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.2] Tool Auto Instagram[PC-Mobile]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [1.3] Tool Auto LinkedIn[PC-Mobile]')
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Trao Đổi Sub   \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [2] Tool TDS TikTok ADB auto follow,tim...')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [2.1] Tool Auto Facebook[PC+Mobile]')
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Tương Tác Chéo \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [3] Tool TTC Facebook[Mobile+PC]')
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [3.1] Tool TTC Facebook[PC Untiblock,Vip]')
print("\033[1;95m║  \033[1;32mTool NUÔI FACEBOOK VIP \033[1;95m║")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [4] Tool Nuôi Facebook[PC]')
print("\033[1;95m║  \033[1;32mTool Tiện ích \033[1;95m║")
in_dong_khung_cau_vong('[TOOL]➩ Nhập Số [5] Tool reg profile Facebook [PC+Mobile]')





chon = str(input('\033[91mTOOL\033[93m➩ \033[96mNhập Số : \033[92m'))
#golike
if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/glttadb.py').text)
elif chon == '1.1':
    exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/glfb.py').text)
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/tdsttadb.py').text)
elif chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/ttcfb.py').text)
elif chon == '4':
	exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/nuoifb.py').text)
elif chon == '5':
	exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/regprofile.py').text)
elif chon == '1.2':
	exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/gljg.py').text)
elif chon == '1.3':
	exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/gllink.py').text)
if chon == '3.1':
	exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/ttcfbunti.py').text)
elif chon == '2.1':
	exec(requests.get('https://raw.githubusercontent.com/Mle28288/Mlevip/refs/heads/main/tdsfb.py').text)

	exec(requests.get('accc').text)
else:
    print("Sai Lựa Chọn")
    exit()
