import string
import random
import datetime

def randWord(minSize = 2, maxSize = 6, chars=string.ascii_lowercase):
    VOWELS = "aeiou"
    LETTERS = "".join(set(chars) - set(VOWELS))
    vowelsNum = random.randint(1, minSize)
    lettersNum = random.randint(1, maxSize - vowelsNum)
    vowels = random.choice(VOWELS)
    letters = "".join(random.choice(LETTERS) for _ in range(lettersNum))
    return mixShuffle(letters, vowels).capitalize()

def mixShuffle(first, second):
    listResult = list(first + second)
    result = "".join(random.sample(listResult, len(listResult)))
    return result

def genName():
    return randWord() + " " + randWord()

def genGender():
    return random.choice("MF")

def genDOB():
    startDate = datetime.date(1920, 1, 1)
    endDate = datetime.date(2021, 8, 1)
    betweenDate = (endDate - startDate).days
    daysSince = random.randrange(betweenDate)
    randomDate = startDate + datetime.timedelta(days=daysSince)
    return randomDate.strftime("%d/%m/%Y")

def genPhone():
    leading = str(random.choice([5, 6, 9]))
    return leading + "".join(random.choice(string.digits) for _ in range(7))

def genEmail():
    TLD = [".com", ".net", ".co"]
    return mixShuffle(randWord(), str(random.randint(0, 9))) + "@" + randWord() + random.choice(TLD)

def genAddr():
    DISTRICTS = ["Wan Chai", "Mong Kok", "Tai Po", "Yuen Long", "Kwun Tong"]
    building = randWord() + " Building"
    street = randWord() + " Road"
    district = random.choice(DISTRICTS)
    return building + ", " + street + ", " + district


def generateDictionary():
    dictionary = {
        "name": genName(),
        "gender": genGender(),
        "dateOfBirth": genDOB(),
        "phoneNumber": genPhone(),
        "email": genEmail(),
        "address": genAddr()    
    }
    return dictionary

print(generateDictionary())