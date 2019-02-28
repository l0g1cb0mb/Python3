import os

def minutes():
    sec = int(input("How many minutes to shutdown the computer?\n"))
    return 60 * sec

def shutdown():
    try:
        min = minutes()
    except ValueError as verr:
        print("The input given must be the type of int")
    else:
        os.system(f"shutdown -s -t {min}")

def cancel_shutdown():
    os.system("shutdown -a")

def user_choice():
    choice = int(input("Your choice: "))
    return choice

def main():
    while(True):
        print("0. Quit", "1. Shutdown", "2. Cancel the shutdown", sep="\n")
        try:
           choice = user_choice()
        except ValueError as verr:
            print("Invalid option, try again!")
        else:
            if 0 <= choice <= 2:
                if choice == 0:
                    return
                elif choice == 1:
                    shutdown()
                    os.system("cls")
                elif choice == 2:
                    cancel_shutdown()
                    os.system("cls")
                
if __name__ == "__main__":				
    main()
