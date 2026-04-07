#import everything
#import faker
from classes import *
from helper import *


#main function
def main_menu():
    # store characters (you currently only generate random ones)
    character_list = []
    file_path = "docs/character_csv.csv"
    while True:
        print("\n=====================================")
        print("ENHANCED RPG CHARACTER MANAGER")
        print("=====================================")

        print("\nDATA & ANALYSIS:")
        print("[1] Character Visualization")
        print("[2] Statistical Analysis")

        print("\nCHARACTER FEATURES:")
        print("[3] Generate Random Character")

        print("\nDATA MANAGEMENT:")
        print("[4] Save Characters to CSV")
        print("[5] Load Characters from CSV")

        print("\n[Q] Quit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            if len(character_list) == 0:
                print("No characters available!")
                continue

            print("\nChoose a character to visualize:")
            for i, char in enumerate(character_list):
                print(f"[{i}] {char.name} ({char.character_class})")

            try:
                index = int(input("Enter index: "))
                char_dict = character_list[index].dictify()

                viz = DataVisualization(char_dict)
                viz.display()
            except:
                print("Invalid selection.")

        elif choice == "2":
            statistical_analysis()

        elif choice == "3":
            new_char = random_char()

            # convert to your Character class so it works with everything
            character_obj = Character(
                new_char.name,
                new_char.clss,
                new_char.species,
                new_char.level,
                r.randint(1, 10),
                r.randint(1, 10),
                r.randint(1, 10),
                r.randint(1, 10)
            )

            character_list.append(character_obj)

            print(f"\nCreated: {character_obj.name} ({character_obj.character_class})")

        elif choice == "4":
            if len(character_list) == 0:
                print("No characters to save!")
                continue


            # convert all characters to dictionaries
            data = [char.dictify() for char in character_list]

            save_csv(data, file_path)
            print("Saved successfully!")

        elif choice == "5":
            data = csv_to_dictionary(file_path)
            if 'error' in data:
                continue
            character_list.clear()
            for entry in data:
                character_list.append(Character(
                    entry["name"],
                    entry["class"],
                    entry["species"],
                    int(entry["level"]),
                    int(entry["strength"]),
                    int(entry["wisdom"]),
                    int(entry["charisma"]),
                    int(entry["intelligence"])
                ))
            print("Characters loaded!")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main_menu()