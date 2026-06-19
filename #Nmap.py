#Nmap
import Nmap
import ipaddress
import shutil
import sys

def display_welcome():
    print('''
          **************************************************************************************************************
          *                                  nmap scanner project                                                      *
          **************************************************************************************************************
          ''')
    
def get_ip_address():
    while True:
        ip = input("Enter your target IP Address: ")
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            print("Invalid IP address. Please try again")

def perform_scan(ip_addr,scan_type):
    if not shutil.which("nmap"):
        print("ERROR: nmap is not installed. Please install nmap first.")
        sys.exit(1)


    sc = nmap.PortScanner()
    scan_option ={
        '1' : ['-sS -sV','tcp'],
        '2' : ['-sU -sV','udp'],
        '3' : ['-sS -sV -p - o -sC','tcp,udp']
    }
         
        
    if scan_type not in scan_option:
        print("Invalid scan type. Please choose a valid option.")
        return
    print("Nmap Version: ",sc.nmap_version())
    print("scanning in Progress...")

    try:
        sc.scan(ip_addr, arguments=scan_option[scan_type][0])

        if ip_addr in sc.all_hosts():
            print("Host is up. Scan Results:")
            proto = scan_option[scan_type][1]
            if proto in sc[ip_addr].all_protocols():
                print(f"{'port':<10} {'state':<10} {'service':<20}")
                for port, info in sc[ip_addr][proto].items():
                    service =  info['name']
                    state = info['state']
                    print(f"{port:<10}{info['name']:<20}{info['state']:<10}")
                else:
                    print("No open ports found.")
        else:
                print("Host is down or no information available.")
    except Exception as e:
            print(f"An error occurred during scanning: {e}")

def get_scan_type():
    print('''
          Please select the type of scan you want to perform:
          1. TCP SYN Scan
          2. UDP Scan
          3. Comprehensive Scan (TCP SYN + UDP + Service Detection)
          ''')
    return input("Enter your choice(1,2,3): ")  
def main():
    display_welcome()
    while True:
        ip_addr = get_ip_address()
        scan_type = get_scan_type()
        perform_scan(ip_addr,scan_type)
        again = input("Do you want to perform another scan? (y/n): ")
        if again.lower() != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()      
