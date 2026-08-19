text = "programming is awesome"

vowels = set("aeiou")
unique_vowels = set(text.lower()) & vowels

print(unique_vowels)