import subprocess
import socket

def nslookup(address):
    try:
        result = socket.gethostbyname(address)
        print(f"NSLookup result: {result}")
    except socket.gaierror as e:
        print(f"NSLookup failed: {e}")

def nslookup_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            address = line.strip()
            nslookup(address)

def ping_host(address):
    try:
        result = subprocess.run(["ping", "-c", "4", address], capture_output=True, text=True, check=True)
        print(f"Ping result for {address}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Ping failed for {address}: {e}")

def ping_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            address = line.strip()
            ping_host(address)

if __name__ == "__main__":
    while True:
        print("\nSelect an option:")
        print("1. NSLookup")
        print("2. Ping")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("\nSelect an option for NSLookup:")
            print("1. NSLookup from a single host")
            print("2. NSLookup from a text file")
            
            nslookup_choice = input("Enter the number of your choice: ")

            if nslookup_choice == "1":
                target = input("Enter the address for NSLookup: ")
                nslookup(target)
            elif nslookup_choice == "2":
                file_path = input("Enter the path of the file containing addresses (one per line): ")
                nslookup_from_file(file_path)
            else:
                print("Invalid choice for NSLookup. Please select a valid option.")
        elif choice == "2":
            print("\nSelect an option for Ping:")
            print("1. Ping a single host")
            print("2. Ping from a text file")
            
            ping_choice = input("Enter the number of your choice: ")

            if ping_choice == "1":
                target = input("Enter the address for Ping: ")
                ping_host(target)
            elif ping_choice == "2":
                file_path = input("Enter the path of the file containing addresses (one per line): ")
                ping_from_file(file_path)
            else:
                print("Invalid choice for Ping. Please select a valid option.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
