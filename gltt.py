try:
    import requests
    import time
    import os 
    import threading
    from art import *
    from colorama import Fore
    from time import sleep
    import json
    import random
    import dns.resolver
    import socket
    from tabulate import tabulate
    import sys
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system('pip install random_user_agent')
    os.system('pip install dnspython')
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
org_socket = socket.getaddrinfo

def google_socket(host, port, family=0, type=0, proto=0, flags=0):
    try:
        info = resolver.resolve(host)
        ip_address = info[0].to_text()
        return org_socket(ip_address, port, family, type, proto, flags)
    except:
        return org_socket(host, port, family, type, proto, flags)

socket.getaddrinfo = google_socket
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)


TOA_DO_FILE = "toa_do.txt"

def lay_toa_do_nut():
    """Lấy tọa độ nút từ người dùng nhập vào hoặc đọc từ file nếu có"""
    if os.path.exists(TOA_DO_FILE):
        try:
            with open(TOA_DO_FILE, "r") as file:
                toa_do = json.load(file)
            print("Sử dụng tọa độ đã lưu:", toa_do)
            return toa_do
        except Exception as e:
            print(f"Lỗi khi đọc tọa độ từ file: {e}, nhập lại tọa độ mới.")

    print("\n=== Cài đặt Tọa độ Nút Bấm ===")
    try:
        follow_x = int(input("Nhập tọa độ X của nút Follow: "))
        follow_y = int(input("Nhập tọa độ Y của nút Follow: "))
        like_x = int(input("Nhập tọa độ X của nút Like: "))
        like_y = int(input("Nhập tọa độ Y của nút Like: "))

        if any(toa_do < 0 for toa_do in [follow_x, follow_y, like_x, like_y]):
            raise ValueError("Tọa độ không thể là số âm")

        toa_do = {
            "follow": (follow_x, follow_y),
            "like": (like_x, like_y)
        }

        # Lưu tọa độ vào file
        with open(TOA_DO_FILE, "w") as file:
            json.dump(toa_do, file)

        print("Tọa độ đã được lưu!")
        return toa_do

    except ValueError as e:
        print(f"Lỗi nhập tọa độ: {str(e)}. Vui lòng nhập số hợp lệ.")
        return None

def kiem_tra_adb():
    """Kiểm tra xem thiết bị có kết nối với ADB hay không"""
    output = os.popen("adb devices").read()
    if "device" in output.split("\n")[1]:  # Dòng thứ hai chứa danh sách thiết bị
        return True
    print("Lỗi: Không tìm thấy thiết bị ADB!")
    return False

def click_tiktok_buttons(toa_do, delay):
    """Click vào nút Follow và thả tim bằng nhấp đúp trên TikTok."""
    if not kiem_tra_adb():
        return False

    try:
        # Click vào nút Follow
        os.system(f"adb shell input tap {toa_do['follow'][0]} {toa_do['follow'][1]}")
        time.sleep(random.uniform(delay, delay + 2))  # Delay ngẫu nhiên để tránh bị phát hiện

        # Nhấp đúp vào màn hình để thả tim (double tap)
        #print("❤️ Nhấp đồng thời vào màn hình để thả tim...")
        x, y = toa_do['like']

        # Chạy 5 lệnh nhấn like đồng thời
        os.system(f"""
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y} & 
            adb shell input tap {x} {y}
        """)

        time.sleep(random.uniform(delay, delay + 1))  # Delay tiếp tục
        return True

    except Exception as e:
        print(f"❌ Lỗi khi thực hiện click ADB: {str(e)}")
        return False
def auto_click():
    """Chạy auto click Follow và Like trong một luồng riêng."""
    while True:
        actual_delay = random.randint(delay_min, delay_max)
        click_tiktok_buttons(toa_do_nut, actual_delay)
        #print(f"Đã click, chờ {actual_delay} giây trước lần tiếp theo...")
        time.sleep(actual_delay)
# Chạy chương trình
# Chạy chương trình liên tục
# Chạy chương trình liên tục trong một luồng riêng
toa_do_nut = lay_toa_do_nut()
if toa_do_nut:
    try:
        delay_min = int(input("Nhập thời gian delay tối thiểu giữa các lần click (giây): "))
        delay_max = int(input("Nhập thời gian delay tối đa giữa các lần click (giây): "))

        # Chạy auto click trong thread
        click_thread = threading.Thread(target=auto_click)
        click_thread.daemon = True  # Chạy nền
        click_thread.start()

    except ValueError:
        print("Lỗi: Delay phải là số nguyên!")

# Các chức năng khác của chương trình vẫn chạy tiếp bình thường

def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            "\033[1;37m\033[1;36m\033[1;35m\033[1;32m\033[1;31m \033[1;34m\033[1;33m\033[1;36m\033[1;36m🍉 - ĐỚP\033[1;36m \033[1;31m\033[1;32m",
            "\033[1;34m\033[1;31m\033[1;37m\033[1;36m\033[1;32m \033[1;35m\033[1;37m\033[1;33m\033[1;32m🍉 - ĐỚP\033[1;34m \033[1;31m\033[1;32m",
            "\033[1;31m\033[1;37m\033[1;36m\033[1;33m\033[1;35m \033[1;32m\033[1;34m\033[1;35m\033[1;37m🍉 - ĐỚP\033[1;33m \033[1;31m\033[1;32m",
            "\033[1;32m\033[1;33m\033[1;34m\033[1;35m\033[1;36m \033[1;37m\033[1;36m\033[1;31m\033[1;34m🍉 - ĐỚP\033[1;31m \033[1;31m\033[1;32m",
            "\033[1;37m\033[1;34m\033[1;35m\033[1;36m\033[1;32m \033[1;33m\033[1;31m\033[1;37m\033[1;34m🍉 - ĐỚP\033[1;37m \033[1;31m\033[1;32m",
            "\033[1;34m\033[1;33m\033[1;37m\033[1;35m\033[1;31m \033[1;36m\033[1;36m\033[1;32m\033[1;37m🍉 - ĐỚP\033[1;36m \033[1;31m\033[1;32m",
            "\033[1;36m\033[1;35m\033[1;31m\033[1;34m\033[1;37m \033[1;35m\033[1;32m\033[1;36m\033[1;33m🍉 - ĐỚP\033[1;33m \033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
                                  
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ", end="\r")

# Rest of your original code remains the same...
# (Including TIKTOKINFO(), banner(), LIST() and the main authentication flow)

def TIKTOKINFO():  
    url1_2 = 'https://gateway.golike.net/api/tiktok-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_tiktok1 = []
    account_id1 = []
    STT = []
    STATUS =[]
    tong = 0
    dem = 0
    i = 1

    for data in checkurl1_2['data']:
        usernametk = data['nickname']
        account_id = data['id']
        user_tiktok1.append(usernametk)
        account_id1.append(account_id)
        STT.append(i)
        STATUS.append(Fore.GREEN + "Hoạt Động" + Fore.RESET)
        
        print(f'\033[1;36m[{i}] \033[1;36m✈ \033[1;97mTài Khoản┊\033[1;32m㊪ :\033[1;93m {usernametk} \033[1;97m|\033[1;32m㊪ :\033[1;93m {STATUS[-1]}')
        
        i += 1

    print('\033[97m════════════════════════════════════════════════')
    choose = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Tài Khoản : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    
    if choose >= 1 and choose <= len(user_tiktok1):
        user_tiktok1 = user_tiktok1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_tiktok1[0] 
        account_id = account_id1[0]
        banner()
        
        job_count = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Số Lượng Job : '))
        DELAY = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập delay : '))
        
        print('\033[97m════════════════════════════════════════════════')
        print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng')

        # Main job processing loop with the enhanced click delay
        
            # Your existing job processing code...
            # When calling click_tiktok_buttons, pass the DELAY parameter:
           

        for i in range(choose):
            url2 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id='+str(account_id)+'&data=null'
            checkurl2 = ses.get(url2,headers=headers).json()
            if checkurl2['status'] ==200:
                linkjob = []
                linkjob = str(checkurl2['data']['link'])
                lenjob = len(checkurl2['data']['link'])
                ads_id = checkurl2['data']['id']
                object_id = checkurl2['data']['object_id']
                type = checkurl2['data']['type']
                os.system("termux-open-url "+str(linkjob[0:lenjob])+"")
                
               

                
                PARAMS = {
                    'ads_id': ads_id,
                    'account_id': account_id,
                    'object_id': object_id,
                    'async': 'true',
                    'data': 'null',
                    'type': type,
                }
                countdown(DELAY)
                url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                time.sleep(1)
                checkurl3 = ses.post(url3,params=PARAMS).json()
                if checkurl3['status'] == 400 :

                        time.sleep(2)

                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                        checkurl3 = ses.post(url3,params=PARAMS).json()
                        if checkurl3['status'] == 200:
                            dem += 1
                            local_time = time.localtime()
                            hour = local_time.tm_hour
                            minute = local_time.tm_min
                            second = local_time.tm_sec

                            # Định dạng giờ, phút, giây
                            h = f"{hour:02d}"
                            m = f"{minute:02d}"
                            s = f"{second:02d}"
                            prices = checkurl3['data']['prices']

                            # Cộng dồn giá trị prices vào tổng tiền
                            tong += prices
                            chuoi = (
                                f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                f"\033[1;33m{tong} vnđ"
                            )
                            print(chuoi) 
                                # prices = checkurl3['data']['prices']
                                # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                        else:

                                    time.sleep(2)

                                    url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                    checkurl3 = ses.post(url3,params=PARAMS).json()
                                    if checkurl3['status'] == 200:
                                        dem += 1
                                        local_time = time.localtime()
                                        hour = local_time.tm_hour
                                        minute = local_time.tm_min
                                        second = local_time.tm_sec

                                        # Định dạng giờ, phút, giây
                                        h = f"{hour:02d}"
                                        m = f"{minute:02d}"
                                        s = f"{second:02d}"
                                        prices = checkurl3['data']['prices']

                                        # Cộng dồn giá trị prices vào tổng tiền
                                        tong += prices
                                        chuoi = (
                                            f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                            f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                            f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                            f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                            f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                            f"\033[1;33m{tong} vnđ"
                                        )
                                        print(chuoi) 
                                            # prices = checkurl3['data']['prices']
                                            # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                        time.sleep(2)

                                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                        checkurl3 = ses.post(url3,params=PARAMS).json()
                                        if checkurl3['status'] == 200:
                                            dem += 1
                                            local_time = time.localtime()
                                            hour = local_time.tm_hour
                                            minute = local_time.tm_min
                                            second = local_time.tm_sec

                                            # Định dạng giờ, phút, giây
                                            h = f"{hour:02d}"
                                            m = f"{minute:02d}"
                                            s = f"{second:02d}"
                                            prices = checkurl3['data']['prices']

                                            # Cộng dồn giá trị prices vào tổng tiền
                                            tong += prices

                                            chuoi = (
                                                f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                                f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                                f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                                f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                                f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                                f"\033[1;33m{tong} vnđ"
                                            )
                                            print(chuoi) 
                                                # prices = checkurl3['data']['prices']
                                                # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    'async': 'true',
                                                    'data': 'null',
                                                    'type': type,
                                                    }
                elif checkurl3['status'] == 200:
                        dem += 1
                        local_time = time.localtime()
                        hour = local_time.tm_hour
                        minute = local_time.tm_min
                        second = local_time.tm_sec

                        # Định dạng giờ, phút, giây
                        h = f"{hour:02d}"
                        m = f"{minute:02d}"
                        s = f"{second:02d}"
                        prices = checkurl3['data']['prices']

                        # Cộng dồn giá trị prices vào tổng tiền
                        tong += prices

                        chuoi = (
                            f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                            f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                            f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                            f"\033[1;31m{type}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                            f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                            f"\033[1;33m{tong} vnđ"
                        )
                        print(chuoi) 
                    
                    # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                else :
                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                    if checkskipjob['status'] == 200:
                        message = checkskipjob['message']
                        print(Fore.RED+str(message))
                        PARAMSr = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
            else : 
                countdown(15)
                print(checkurl2['message'])
                skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                if checkskipjob['status'] == 200:
                    message = checkskipjob['message']
                    print(Fore.RED+str(message))
                    PARAMSr = {
                    'ads_id' : ads_id,
                    'account_id' : account_id,
                    'object_id' : object_id ,
                    'async': 'true',
                    'data': 'null',
                    'type': type,
                    }

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner_text = """
    ─────────────────────────────────────────
    🎀✨ Chào mừng bạn đến với Tool ✨🎀
    ─────────────────────────────────────────
    🌸 Chúc bạn một ngày vui vẻ và nhiều may mắn! 🌸
    🐱 Mèo con chúc bạn code không lỗi! 🐱
    ─────────────────────────────────────────
    """
    
    for X in banner_text:
        sys.stdout.write(X)
        sys.stdout.flush()
        time.sleep(0.00125)

banner()
def LIST():
    banner()
os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNHẬP Authorization Golike : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()

ses = requests.Session()
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; XT1045 Build/[KXB20.9|KXC21.5]) AppleWebKit/601.38 (KHTML, like Gecko) Chrome/48.0.2780.100 Mobile Safari/535.6",
"android|Mozilla/5.0 (Linux; Android 6.0; Nexus 6X Build/MDB08L) AppleWebKit/601.19 (KHTML, like Gecko) Chrome/50.0.2717.179 Mobile Safari/534.2",
"android|Mozilla/5.0 (Android; Android 5.1.1; SAMSUNG SM-G920M Build/LRX22G) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/48.0.3528.122 Mobile Safari/533.8",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G928I Build/MMB29K) AppleWebKit/602.37 (KHTML, like Gecko) Chrome/49.0.2276.245 Mobile Safari/535.1",
])
try:
    headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
                'Referer':'https://app.golike.net/',
                'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':"Windows",
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-site',
                'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
                'User-Agent':User_Agent,
                "Authorization" : file,
                'Content-Type':'application/json;charset=utf-8'            
    }

    url1 = 'https://gateway.golike.net/api/users/me'
    checkurl1 = ses.get(url1,headers=headers).json()
except requests.exceptions.InvalidHeader:
    os.remove('user.txt')
    #user
if checkurl1['status']== 200 :
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        LIST()
        ses.headers.update(headers)
        username = checkurl1['data']['username']
        coin = checkurl1['data']['coin']
        user_id = checkurl1['data']['id']
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
        print(Fore.RED+'\033[97m════════════════════════════════════════════════')
        print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool TikTok\033[1;33m")
        print(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mNhập 2 Để Xóa Authorization Hiện Tại')
        choose = int(input(Fore.WHITE+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Lựa Chọn : '))
        if choose == 1:
                os.system('cls' if os.name== 'nt' else 'clear')
                LIST()
                ses.headers.update(headers)
                username = checkurl1['data']['username']
                coin = checkurl1['data']['coin']
                user_id = checkurl1['data']['id']
                print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
                print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))  
                print('\033[97m════════════════════════════════════════════════')
                TIKTOKINFO()
        elif choose == 2:
                os.remove('user.txt')
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')










    
