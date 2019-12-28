import input

newInput = input.input

woorden = list(newInput.split("\n"))
vowels = ["a", "e", "i", "o", "u"]

for woord in woorden:
    optelling =0
    for vowel in vowels:
        if vowel in woord:
            optelling = optelling + 1
    print(optelling)