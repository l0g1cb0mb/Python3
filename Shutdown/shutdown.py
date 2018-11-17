import os

def shutdown():
    sec = int(input("Za ile minut ma nastąpić wyłączenie komputera?\n"))
    min = 60 * sec
    os.system(f"shutdown -s -t {min}")

def cancel_shutdown():
    os.system("shutdown -a")

def main():
    while(True):
        print("0. Wyjście", "1. Wyłącz komputer", "2. Anuluj wyłączanie komputera", sep="\n")
        x = int(input("Wybierz co chcesz zrobić: "))

        if 0 <= x <= 2:
            if x == 0:
                break
            elif x == 1:
                shutdown()
                os.system("cls")
            elif x == 2:
                cancel_shutdown()
                os.system("cls")
				
main()
