# 1. Built-in Functions on Strings (Immutable)
s = " Hello World "
# len()
# 👉 Returns number of characters in string.

print(len(s))       # 13 (includes spaces)
print(len(""))      # 0 (empty string)
try:
    print(len(123)) # ❌ int has no length
except TypeError as e:
    print("Error:", e)

# 🔸 str.upper()
# 👉 Converts all letters to uppercase.

print(s.upper())    # " HELLO WORLD "

# 🔸 str.lower()
# 👉 Converts all letters to lowercase.

print(s.lower())    # " hello world "

# 🔸 str.title()
# 👉 Capitalizes first letter of each word.

print(s.title())    # " Hello World "

# 🔸 str.strip()
# 👉 Removes spaces from both sides.

print(s.strip())    # "Hello World"
print("****hi****".strip("*"))  # "hi"

# 🔸 str.replace(old, new)
# 👉 Replaces a substring with another.

print(s.replace("World", "Python"))  # " Hello Python "

# 🔸 str.split()
# 👉 Splits string into list (default: spaces).

print(s.split())      # ['Hello', 'World']
print("a,b,c".split(","))  # ['a','b','c']

# 🔸 "sep".join(list)
# 👉 Joins list of strings with a separator.

print("-".join(["Hi", "There"]))  # "Hi-There"
try:
    print("-".join([1, 2]))  # ❌ non-string values
except TypeError as e:
    print("Error:", e)

# 🔸 str.find()
# 👉 Returns index of substring, or -1 if not found.

print(s.find("o"))   # 5
print(s.find("z"))   # -1

# 🔸 str.index()
# 👉 Same as find(), but raises error if not found.

print(s.index("o"))  # 5
try:
    print(s.index("z"))  # ❌ not found
except ValueError as e:
    print("Error:", e)

# 🔸 str.count()
# 👉 Counts occurrences of substring.

print(s.count("l"))   # 3

# 🔸 String checks
# 👉 Return True/False.

print("abc".isalpha())    # True
print("abc1".isalpha())   # False
print("123".isdigit())    # True
print("12a".isdigit())    # False
print("abc123".isalnum()) # True
print(s.startswith(" He")) # True
print(s.endswith("ld "))   # True


# ✅ Summary (Strings):
# Never modify original string.

# Errors: index() (if substring not found), join() (if non-string values).

# 🔹 2. Built-in Functions on Sets (Mutable)
# Let’s take:

s = {10, 20, 30}

# 🔸 len()
# 👉 Returns number of elements.

print(len(s))    # 3
print(len(set())) # 0

# 🔸 set.add(x)
# 👉 Adds element to set.

s.add(40)
print(s)   # {40, 10, 20, 30}

# 🔸 set.remove(x)
# 👉 Removes element if present. Raises error if missing.

s.remove(20)
print(s)   # {40, 10, 30}
try:
    s.remove(99)  # ❌ not found
except KeyError as e:
    print("Error:", e)

# 🔸 set.discard(x)
# 👉 Removes element if present, no error if missing.

s.discard(99)
print(s)   # {40, 10, 30}

# 🔸 set.pop()
# 👉 Removes and returns a random element.

print(s.pop())   # removes random
print(s)
try:
    empty_set = set()
    empty_set.pop()  # ❌ empty set
except KeyError as e:
    print("Error:", e)

# 🔸 set.clear()
# 👉 Removes all elements.

s.clear()
print(s)   # set()

# 🔸 set.update(iterable)
# 👉 Adds multiple elements.

a = {1, 2, 3}
a.update([6, 7])
print(a)   # {1, 2, 3, 6, 7}
try:
    a.update(100)  # ❌ not iterable
except TypeError as e:
    print("Error:", e)

# 🔸 set.union(other)
# 👉 Returns new set with all elements.

b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7}

# 🔸 set.intersection(other)
# 👉 Returns common elements.

print(a.intersection(b))  # {3}

# 🔸 set.difference(other)
# 👉 Elements in a but not in b.

print(a.difference(b))  # {1, 2, 6, 7}

# 🔸 set.symmetric_difference(other)
# 👉 Elements in either set but not both.

print(a.symmetric_difference(b))  # {1, 2, 4, 5, 6, 7}

# 🔸 Subset, Superset, Disjoint
# 👉 Relationship checks.

print({1,2}.issubset({1,2,3}))     # True
print({1,2,3}.issuperset({1}))     # True
print({1,2}.isdisjoint({3,4}))     # True