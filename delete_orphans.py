import subprocess
import getpass

# Ask the user for the administrator password
password = getpass.getpass(prompt='Enter Administrator Password: ')

# Set the directory to change to
directory = 'C:\\Users\\Username\\Documents'

# Construct the command to run PowerShell as an administrator and change directory
cmd = f'start powershell -NoExit -Command "Set-Location \'{directory}\'"'
cmd = ['runas', '/user:Administrator', cmd]

# Use Popen to launch PowerShell and pass the password
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
p.stdin.write(f"{password}\n".encode())
p.stdin.flush()

# Read the output from PowerShell
output, err = p.communicate()

# Print the output and any errors
print(output.decode())
print(err.decode())
