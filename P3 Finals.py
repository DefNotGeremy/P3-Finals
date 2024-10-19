def main():
    print("Dialogue here")
    print("Select option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. End story")

    story1 = "Dialogue 1"
    story2 = "Dialogue 2"
    story3 = "Dialogue 3"
    continue1 = "Continue 1"

    choice = input("Enter choice (1/2/3/4): ")
                
    if choice == '1':
        print(story1, continue1)

    elif choice == '2':
        print(story2, continue1)

    elif choice == '3':
        print(story3, continue1)

    elif choice == '4':
        print("User has left")
        exit()

    print("Select option:")
    print("1. Option 1")
    print("2. Option 1")
    print("3. Option 1")
    print("4. End story")

    story4 = "Dialogue 4"
    story5 = "Dialogue 5"
    story6 = "Dialogue 6"
    continue2 = "Continue 2"
    continue3 = "Continue 3"

    choice = input("Enter choice (1/2/3/4): ")
            
    if choice == '1':
        print(story4, continue2)

    elif choice == '2':
        print(story5, continue2)
        flirtt()

    elif choice == '3':
        print(story6, continue3)
        lie()

    elif choice == '4':
        print("User has left")
        exit()

def flirt():
    story7 = "Dialogue 7"
    continue4 = "Continue 4"
    print(story7, continue4)
    flirt_options()

def flirt_options():
    print("Select option:")
    print("1. ")
    print("2. ")
    print("3. ")
    
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print("Text here")
    elif choice == '2':
        print("Text here")
    elif choice == '3':
        print("Text here")
        exit()

def lie():
    story8 = "Dialogue 8"
    continue5 = "Continue 5"
    print(story8, continue5)
    lie_options()

def lie_options():
    print("Select option:")
    print("1. ")
    print("2. ")
    print("3. ")

    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print("Text here")
    elif choice == '2':
        print("Text here")
    elif choice == '3':
        print("Text here")
        exit()


if __name__ == "__main__":
    main()
