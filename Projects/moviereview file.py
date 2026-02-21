class Review:
    @staticmethod
    def menu():
        print("Give Movie Review")
        print("1. Read and analyse notes")
        print("2. Create new notes")
        print("3. Modify existing notes")
        print("4. Exit")

        a = int(input("Enter number: "))

        if a == 1:
            path = input("Enter file path: ").strip('"')
            try:
                with open(path, "r") as file:
                    data = file.readlines()
                    print("\n--- File Content ---")
                    for line in data:
                        print(line.strip())
            except FileNotFoundError:
                print("File not found ")

        elif a == 2:
            path = input("Enter file path to create: ")
            text = input("Write note: ")

            with open(path, "w") as file:
                file.write(text)
            print("File created ")

        elif a == 3:
            path = input("Enter file path to modify: ")
            text = input("Add new content: ")

            with open(path, "a") as file:
                file.write("\n" + text)
            print("File updated ")

        elif a == 4:
            print("Exiting")
        else:
            print("Invalid choice")


# run
Review.menu()