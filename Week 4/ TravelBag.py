room_items = ["toothbrush", "jacket", "shoes", "Playstation", "book", "snacks", "hat", "phone charger"]
travel_bag = []
print("Items in your room:")
for i, item in enumerate(room_items):
    print(f"{i}: {item}")
print("\nPack your bag! Type the index of the item you want to pack. Type 'done' when finished.\n")
while True:
    choice = input("Enter the index of the item to pack (or 'done'): ").strip()
    if choice.lower() == "done":
        break
    elif choice.isdigit():
        index = int(choice)
        if 0 <= index < len(room_items):
            item = room_items.pop(index)
            travel_bag.append(item)
            print(f"Added '{item}' to your travel bag.")
        else:
            print("Invalid index. Try again.")
    else:
        print("Please enter a number or 'done'.")
luggage = tuple(travel_bag)
travel_bag.clear()
print("\nYour packed luggage contains:")
for item in luggage:
    print(f"- {item}")
print(f"Total items packed: {len(luggage)}")