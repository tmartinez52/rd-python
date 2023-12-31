import argparse
import time 

def main():
    parser = argparse.ArgumentParser(description='Command-line utility example')
    parser.add_argument('-u', '--username', help='Username')
    parser.add_argument('-p', '--password', help='Password')
    parser.add_argument('-ip', '--ip_address', help='IP address')

    args = parser.parse_args()

    username = args.username
    password = args.password
    ip_address = args.ip_address

    # Do something with the parameters
    print(f"Username: {username}")
    time.sleep(5)
    print(f"Password: {password}")
    time.sleep(5)
    print(f"IP Address: {ip_address}")

if __name__ == '__main__':
    main()
