'''
Write a function get_vowels() that takes a string and returns a list of all the vowels in it, using a list comprehension with a filtering condition. Include both uppercase and lowercase vowels.
Use a list comprehension with an if clause to filter characters
Find vowels regardless of their case
Preserve the original case of each vowel in the result


get_vowels("hello")
outputs
['e', 'o']
get_vowels("Hello World")
outputs
['e', 'o', 'o']
get_vowels("AEIOU")
outputs
['A', 'E', 'I', 'O', 'U']
get_vowels("rhythm")
outputs
[]


'''

def get_vowels(text):
    """Return a list of vowels found in the text."""
    return [i  for i in text  if i.lower() in {"a","e","i","o","u"}] # [i  for i in text  if i.lower() in "aeiou"]


