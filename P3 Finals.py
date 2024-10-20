#Start of the story
def main():
    print("Start of story")
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
        continuation()

    elif choice == '2':
        print(story2, continue1)
        continuation()

    elif choice == '3':
        print(story3, continue1)
        continuation()

    elif choice == '4':
        print("User has left")
        exit()
    
    else:
        print("Invalid choice. Please try again.")
        main()

def continuation():
    print("Select option:")
    print("1. Option 1") 
    print("2. Option 2")
    print("3. Option 3")
    print("4. End story")

    choice = input("Enter choice (1/2/3/4): ")
            
    if choice == '1':
        story4 = "Dialogue 4"
        continue2 = "Continue 2"
        print(story4, continue2)
        friendship()

    elif choice == '2':
        story5 = "Story 5"
        continue3 = "Continue 3"
        print(story5, continue3)
        flirt()

    elif choice == '3':
        story6 = "Dialogue 6"
        continue4 = "Continue 4'"
        print(story6, continue4)
        lie()

    elif choice == '4':
        print("User has left")
        exit()
    
    else:
        print("Invalid choice. Please try again.")
        continuation()

#friendship route
def friendship():
    print("Select option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. End story")

    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print("")
    
    elif choice == '2':
        print("")
    
    elif choice == '3':
        print("User has left")
        exit()

    else:
        print("Invalid choice. Please try again.")
        friendship()

#romance route
def flirt():
    print("Select option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. End story")
    
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print("")
    
    elif choice == '2':
        print("")
    
    elif choice == '3':
        print("User has left")
        exit()
    
    else:
        print("Invalid choice. Please try again.")
        flirt()

#creepy route
def lie():
    print("Select option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. End story")

    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print("")
    
    elif choice == '2':
        print("")
    
    elif choice == '3':
        print("User has left")
        exit()
    
    else:
        print("Invalid choice. Please try again.")
        lie()

if __name__ == "__main__":
    main()
