import dictionary

print(dictionary.d)
text = "I drive a red car in the city with a friend to go to the cinema"
translate = ""
words = text.split()
for w in words:
    translate = translate + dictionary.d[w]
    translate = translate + " "

print(translate)




