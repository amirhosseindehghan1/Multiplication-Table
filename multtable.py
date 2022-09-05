#This program prints a multiplication table.
# its for FUN =))
def main():
    
    def loop():
        global multnum
        multnum= int(input("Enter an integer between 1 and 10:"))

        if multnum ==1:
             print("1")
        elif multnum==2:
             print("1 2\n2 4")
        elif multnum==3:
             print("1 2 3\n2 4 6\n3 6 9")
        elif multnum==4:
             print("1 2 3 4\n2 4 6 8\n3 6 9 12\n4 8 12 16")
        elif multnum==5:
             print("1 2 3 4 5\n2 4 6 8 10\n3 6 9 12 15\n4 8 12 16 20\n5 10 15 20 25")
        elif multnum==6:
             print("1 2 3 4 5 6\n2 4 6 8 10 12\n3 6 9 12 15 18\n4 8 12 16 20 24\n5 10 15 20 25 30\n6 12 18 24 30 36")
        elif multnum==7:
             print("1 2 3 4 5 6 7\n2 4 6 8 10 12 14\n3 6 9 12 15 18 21\n4 8 12 16 20 24 28\n5 10 15 20 25 30 35\n6 12 18 24 30 36 42\n7 14 21 28 35 42 49")
        elif multnum==8:
            print("1 2 3 4 5 6 7 8\n2 4 6 8 10 12 14 16\n3 9 12 15 18 21 24\n4 8 12 16 20 24 28 32\n5 10 15 20 25 30 35 40\n6 12 18 24 30 36 42 48\n7 14 21 28 35 42 49 56\n8 16 24 32 40 48 56 64")
        elif multnum==9:
            print("1 2 3 4 5 6 7 8 9\n2 4 6 8 10 12 14 16 18\n3 6 9 12 15 18 21 24 27\n4 8 12 16 20 24 28 32 36\n5 10 15 20 25 30 35 40 45\n6 12 18 24 30 36 42 48 54\n7 14 21 28 35 42 49 46 63\n8 16 24 32 40 48 56 64 72\n9 18 27 36 45 54 63 72 81")
        elif multnum==10:
            print("1 2 3 4 5 6 7 8 9 10\n2 4 6 8 10 12 14 16 18 20\n3 6 9 12 15 18 21 24 27 30\n4 8 12 16 20 24 28 32 36 40\n5 10 15 20 25 30 35 40 45 50\n6 12 18 24 30 36 42 48 54 60\n7 14 21 28 35 42 49 46 63 70\n8 16 24 32 40 48 56 64 72 80\n9 18 27 36 45 54 63 72 81 90\n10 20 30 40 50 60 70 80 90 100")
        else:
            print("\nIncorrect menu selection, please try again\n")

    def menu():
        print("=====================")
        print("Multiplication Tables")
        print("=====================")
        print("1) Create a multiplication table")
        print("2) Quit the Program")
        global choice
        choice= int(input("Please select an option from the menu above:"))
        if choice == 1:
            loop()
            menu()
        elif choice == 2:
            print("Thank you for using Multiplication Tables")
        else:
            print("\nIncorrect menu selection, please try again\n")
            menu()
    
    menu()
        
                
main()
