# -----------------------------
# Solution to Day 1 Task
# -----------------------------
# Simple introductory print statement
print("Hello, AI World! My journey begins today.")


# -----------------------------
# Solution to Day 2 Task
# -----------------------------
# Storing personal details in variables
name = 'Bryan'
age = 30   # not real age
height = 1.8   # not real height (in meters)

# Using f-string for better readability
long_sentence = f"My name is {name}, I am {age} years old and I am {height} meters tall"

# Using string concatenation (less clean compared to f-string above)
sentence = "My name is "+ name + ", I am "+ str(age) + " years old and I am " + str(height) + " meters tall"

# Printing both versions (they give the same output)
print(long_sentence) 
print(sentence) 


# -----------------------------
# Solution to Day 3 Task
# -----------------------------
print('Here is a value detection program!')

# Taking user input as string
num_as_str = input("Enter a value: ")

# Converting input to integer (⚠️ will error if input is not a number)
num = int(num_as_str)

# Checking whether number is positive, negative, or zero
if num > 0:
	print('Positive')
elif num < 0:
	print('Negative')
else:
	print('Zero')
	

# -----------------------------
# Solution to Day 4 Task
# -----------------------------
print('Here is a list of my Favorite Anime!')

# Creating a list of anime titles
animes = ['Blue Lock', 'Naruto', 'Death Note', 'Classroom of Elite', 'Solo Leveling']

# Printing the whole list
print(animes)

# Printing the first anime in the list (index 0)
print(animes[0])

# Updating the 3rd anime in the list
animes[2] = 'Sakamoto Days'

# Adding a new anime to the list
animes.append('Spy X Family')

# Printing the updated list
print(animes)


# -----------------------------
# Solution to Day 5 Task
# -----------------------------
print('Here are the animes I love!')

# Looping through the list and printing each anime
for anime in animes:
	print(f"\nAnime: {anime}")
	
# Challenge in Day 5 Task
# Creating a list that stores the length of each anime title
anime_lengths = []
for anime in animes:
	length_of_anime_name = len(anime)
	anime_lengths.append(length_of_anime_name)

# Printing the list of lengths
print(f'Here is the list of the lengths of the Titles of the Anime: {anime_lengths}')


# -----------------------------
# Solution to Day 6 Task
# -----------------------------
# Creating a dictionary to represent a fake profile
my_fake_profile = {
	'name' : 'James',
	'age' : 26,
	'country' : 'Canada',
	'fav_lang' : 'Python',
}

# Accessing and printing a specific value from dictionary
print(f"My favorite programming language is {my_fake_profile['fav_lang']}")

# Adding a new key-value pair to the dictionary
my_fake_profile['is_learning_AI'] = True

print("\nPrinting my entire profile:") # Just a helpful header

# Looping through dictionary items and printing each key-value pair
for key, value in my_fake_profile.items():
    print(f"{key}: {value}")


# -----------------------------
# Day 7 Task
# Personal Information Manager
# -----------------------------
# Creating a dictionary with personal details
personal_info = {
	'name' : 'John',
	'age' : 23,
	'gender' : 'Male',
	'fav_food' : 'Rice',
	'fav_snack' : 'Popcorn',
}

# List of hobbies
hobbies = ['Singing', 'Cooking', 'Drawing', 'Reading Manga', 'Sleeping']

# Loop through hobbies and print them
for hobby in hobbies:
	print(f'I love {hobby}')

# Get the person's age from the dictionary
age = personal_info['age']

# Provide life-stage advice based on age
if age < 18:
    print('You are still a minor. Focus on studying and hobbies!')
elif age < 30:
    print('You are young — build your career and explore opportunities.')
elif age < 50:
    print('Balance work, family, and personal growth.')
else:
    print('Stay healthy and enjoy life to the fullest!')
