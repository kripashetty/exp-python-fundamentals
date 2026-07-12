'''
Write a function get_vowels() that takes a string and returns a list of all the vowels in it, using a list comprehension with a filtering condition. Include both uppercase and lowercase vowels.
'''

def get_vowels(text):
    """Return a list of vowels found in the text."""
    return [i  for i in text  if i.lower() in {"a","e","i","o","u"}] # [i  for i in text  if i.lower() in "aeiou"]


