import socket
import time

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout after 1 second
    try:
        sock.connect((ip, port))
        return True
    except:
        return False
    finally:
        sock.close()

def main():
    print("=== Simple Port Scanner ===")
    target_ip = input("Enter target IP address: ")
    ports = input("Enter ports to scan (comma separated, e.g. 22,80,443): ")
    port_list = [int(p.strip()) for p in ports.split(",")]

    print(f"\nScanning {target_ip}...\n")
    start_time = time.time()

    for port in port_list:
        if scan_port(target_ip, port):
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED or FILTERED")

    end_time = time.time()
    print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")

if __name__ == "__main__":
    main()