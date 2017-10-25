"""
======================================================================
Homework 4
Released: 2017-10-17
Due Date: 2017-10-24, EoD
They told me I could be anything...
...so I became void*.
======================================================================
"""


# is unique
def is_unique(word):
	"""
	Given a string, return true if the string's characters are unique.
	Args:
		(str) word: the input string.

	Returns:
		(bool) True if the string's characters are unique, False otherwise.
	"""


	word = word.replace(" ", "").lower()

	total = 0

	for l in word:
		count = word.count(l)
		if count > 1:
			total += count
	if total > 0:
		return False
	else:
		return True


# Counting Anagrams
def count_anagrams(arr, uniq):
	"""
	Given a list of strings, returns the exact anagrams of uniq in the list.

	Args:
		(List[str]) arr:  a list of strings.
		(str)       uniq: a string.

	Returns:
		(int) the number of anagrams of uniq in arr.
	"""
	count = 0
	for word in arr:
		if sorted(uniq.lower()) == sorted(word.lower()):
			count += 1
	return count



# Anagram of Palindrome
def anagram_of_palindrome(word):
	"""
	Given a string, return true if the string is an anagram of a palindrome.
	Args:
		(str) word: the input string

	Returns:
		(bool) whether or not the input string is an anagram of a palindrome.
	"""
	oddCount = 0
	isPalin = True
	for letter in word:
		if word.count(letter) % 2 == 1:
			oddCount += 1
	if oddCount > 1 and len(word) > 0:
		isPalin = False
	return isPalin


# Reverse Dictionary
def reverse_dictionary(d):
	"""
	Given a dictionary d, reverse its keys and values.
	The values will all be unique.

	Args:
		(Dict[Any, Any]) d: the dictionary.
	Returns:
		(Dict[Any, Any]) a dictionary where the keys of d are its values and vice-versa.
	"""
	newdict = {}
	for key, value in d.items():
		for val in value:
			newdict.setdefault(val, []).append(key)


# Alphabet Finder
def alphabet_finder(sentence):
	"""
	Given a string, returns the shortest substring that:
		1. starts from the beginning of the string
		2. contains all the letters of the alphabet (case insensitive)
	If this is never true, return None.

	Args:
		(str) sentence: the input string
	Returns:
		(str) the shortest substring of sentence that satisfies both (1) and (2).
	"""
	lastPos = -1
	sentence2 = sentence.upper()
	alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for letter in range( len(sentence2)):
		if sentence2[letter:letter + 1] in alpha:
			alpha.remove(sentence2[letter:letter + 1])
		else:
			if len(alpha) == 0:
				lastPos = letter
				break
	if lastPos != -1:
		return sentence[0: lastPos]
	else:
		return None


# Happy Numbers
def square(x):
	return int(x) * int(x)


def happy(number):
	return sum(map(square, list(str(number))))


def is_happy(number):
	seen_numbers = set()
	while number > 1 and (number not in seen_numbers):
		seen_numbers.add(number)
		number = happy(number)
	return number == 1


def happy_numbers(n):
	"""
	Given n, return the number of happy numbers between 1 and n (inclusive).
	https://en.wikipedia.org/wiki/Happy_number
	Args:
		(int) n: the upper bound.

	Returns:
		(int) the number of happy numbers from 1 to n.
	"""
	count = 0
	for num in range(1, n + 1):
		if is_happy(num):
			count = count + 1
	return count