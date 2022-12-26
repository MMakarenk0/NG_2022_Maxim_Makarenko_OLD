def srt(List):
    List.sort()
    print(List)

def getCount(List):
    print("Number of words: " + str(len(List)))
    List1 = list()
    for word in List:
        for letter in word:
            List1.append(letter)
    print("Number of letters: " + str(len(List1)))

def getVowAndCon(List):
    List1 = list()
    for word in List:
        for letter in word: 
            List1.append(letter)
    def filterVow(List1):
        vowels = ['a', 'e', 'i', 'o', 'u']
        return True if List1 in vowels else False
    def filterCon(List1):
        vowels = ['a', 'e', 'i', 'o', 'u']
        return False if List1 in vowels else True
    vow = filter(filterVow, List1)
    con = filter(filterCon, List1)
    vowList = list(vow)
    conList = list(con)
    print("Vowels: " + str(vowList))
    print("Сonsonants: " + str(conList))

def reverseList(List):
    List1 = list()
    for word in reversed(List):
        List1.append(word)
    print("Reversed text: " + str(List1))

def getWordWithIndex(List):
    index = int(input("Enter word number: "))
    print("The word with number " + str(index) + " is: " + List[index-1])


    
while True: 
    txt = input("Enter string: ")
    List = list(txt.split())
    print("=================================")
    print("What should we do? ")
    print('"1" to sort.\n"2" to get count of words and letters.\n"3" to get vowels and consonants.\n"4" to write words in reverse order.')
    nextStep = input('"5" to print word by number.\n"6" to enter the string again.\n"7" to exit the program.\n')
    if nextStep == '1':
        srt(List)
    elif nextStep == '2':
        getCount(List)
    elif nextStep == '3':
        getVowAndCon(List)
    elif nextStep == '4': 
        reverseList(List)
    elif nextStep == '5':
        getWordWithIndex(List)
    elif nextStep == '6':
        continue
    elif nextStep == '7':
        break
    
