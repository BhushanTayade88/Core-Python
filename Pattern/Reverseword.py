word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("")
a=word[::-1]
print(a)

for char in range(len(word)-1,-1,-1):
  print(char,end="")
print("")


