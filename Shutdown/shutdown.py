import os

def shutdown():
    sec = int(input("How many minutes to shutdown the computer?\n"))
    min = 60 * sec
    os.system(f"shutdown -s -t {min}")

def cancel_shutdown():
    os.system("shutdown -a")

def main():
    while(True):
        print("0. Quit", "1. Shutdown", "2. Cancel the shutdown", sep="\n")
        choice = int(input("Your choice: "))

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
