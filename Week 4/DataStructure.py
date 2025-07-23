snacks = ["Hot Cheetos", "Oreos", "Takis", "Trail Mix", "Popcorn"]
# Modify the list: replace "Takis" with "Gummy Bears"
snacks[2] = "Gummy Bears"
# Tuple of 5 colleges (tuples are immutable)
colleges = ("UCLA", "Stanford", "UC Berkeley", "Harvard", "NYU")
# We cannot modify tuples, so we just print as-is
# Set of 5 random facts (sets are mutable but unordered)
random_facts = {"Water is wet", "The Earth is round", "Dogs bark", "2+2=4", "Fire is hot"}
# Modify the set: remove one fact and add a new one
random_facts.remove("2+2=4")
random_facts.add("Python is fun")
# Dictionary about a car (dictionaries are mutable)
car = {
    "make": "Honda",
    "model": "Civic",
    "year": 2022,
    "color": "blue",
    "electric": False
}
# Modify the dictionary: change color and year
car["color"] = "red"
car["year"] = 2024
# Print all data structures
print("Favorite Snacks (List):", snacks)
print("Colleges (Tuple):", colleges)
print("Random Facts (Set):", random_facts)
print("Car Info (Dictionary):", car)






