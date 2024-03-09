import subprocess

def create_user(username, password):
    command = f"net user {username} {password} /add"
    subprocess.run(command, shell=True)

def add_user_to_group(username, group_name):
    command = f"net localgroup {group_name} {username} /add"
    subprocess.run(command, shell=True)

def set_file_permissions(path, username, access_type):
    command = f"icacls {path} /grant {username}:{access_type}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    new_username = "newuser"
    new_password = "password123"
    new_group_name = "Administrators"
    file_path = "C:\\example\\file.txt"
    access_type = "F"  # Full control

    create_user(new_username, new_password)
    add_user_to_group(new_username, new_group_name)
    set_file_permissions(file_path, new_username, access_type)
