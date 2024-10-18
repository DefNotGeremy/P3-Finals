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

    elif choice == '3':
        print(story6, continue3)

    elif choice == '4':
        print("She is now dead.")


if __name__ == "__main__":
    main()