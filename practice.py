# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("Name: {0}\tAge: {1}\t".format(name, age), \
#         lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("Name: {0}\tAge: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("A", 20, "Python", "Java", "C", "C++", "C#", "Javas")
profile("B", 25, "Kotlin", "Swift", "", "", "")
