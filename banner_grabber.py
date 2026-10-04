#!/usr/bin/env python3
"""Banner Grabber - IP va portga ulanib, serverning birinchi javobini (banner) o'qiydi."""
import socket
import ipaddress

TIMEOUT = 3  # soniya


def get_ip():
    while True:
        text = input("IP manzil kiriting (masalan 127.0.0.1): ").strip()
        if text.lower() == "localhost":
            text = "127.0.0.1"
        try:
            return str(ipaddress.IPv4Address(text))
        except ValueError:
            print("[!] Noto'g'ri IPv4 manzil. Qaytadan urinib ko'ring.")


def get_port():
    while True:
        text = input("Port raqami (1-65535): ").strip()
        if text.isdigit() and 1 <= int(text) <= 65535:
            return int(text)
        print("[!] Port 1 dan 65535 gacha butun son bo'lishi kerak.")


def grab_banner(ip, port):
    """Ulanadi va bannerni qaytaradi. Banner kelmasa, bo'sh matn qaytaradi."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(TIMEOUT)
        sock.connect((ip, port))
        try:
            data = sock.recv(1024)          # SSH, FTP, SMTP o'zi gapiradi
        except socket.timeout:
            try:                            # HTTP kabi servislar so'ralishini kutadi
                sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                data = sock.recv(1024)
            except socket.timeout:
                return ""
        return data.decode("utf-8", errors="replace").strip()


def main():
    print("=" * 50)
    print(" BANNER GRABBER (faqat o'z/ruxsat berilgan tizimlar uchun)")
    print("=" * 50)
    while True:
        ip = get_ip()
        port = get_port()
        print(f"\n[*] {ip}:{port} ga ulanilmoqda...")
        try:
            banner = grab_banner(ip, port)
            print("-" * 50)
            print(f" Manzil : {ip}")
            print(f" Port   : {port}")
            print(f" Holat  : OCHIQ")
            if banner:
                print(" Banner :")
                for line in banner.splitlines():
                    print(f"   {line}")
            else:
                print(" Banner : server javob qaytarmadi")
            print("-" * 50)
        except ConnectionRefusedError:
            print(f"[X] Port {port} YOPIQ (ulanish rad etildi).")
        except socket.timeout:
            print(f"[X] Timeout: {ip}:{port} {TIMEOUT} soniyada javob bermadi.")
        except OSError as e:
            print(f"[X] Tarmoq xatosi: {e}")

        again = input("\nYana tekshiramizmi? (h/y): ").strip().lower()
        if again not in ("h", "ha", "y", "yes"):
            print("Dastur tugadi.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDastur to'xtatildi.")
