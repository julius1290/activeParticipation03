class Language:

    name = str

    def __init__(self, name=str):
        self.name = name


class Person:

    languages = list

    def __init__(self, languages=list):
        self.languages = languages


spanish = Language("spanish")
french = Language("french")
english = Language("english")

conference_persons = list()
for i in range(180):
    conference_persons.append(Person([english]))
for i in range(122):
    conference_persons.append(Person([english, french]))
for i in range(24):
    conference_persons.append(Person([french]))
for i in range(42):
    conference_persons.append(Person([french, spanish]))
for i in range(6):
    conference_persons.append(Person([spanish]))
for i in range(60):
    conference_persons.append(Person([spanish, english]))
for i in range(18):
    conference_persons.append(Person([spanish, english, french]))
for i in range(48):
    conference_persons.append(Person([]))

print(len(conference_persons))

counter_no_language = 0
counter_english_spanish = 0

for pers in conference_persons:
    if pers.languages.count(spanish) and pers.languages.count(french) and pers.languages.count(english) == 0:
        counter_no_language += 1
    if pers.languages.count(spanish) and pers.languages.count(english) and not pers.languages.count(french) == 1:
        counter_english_spanish += 1

print(counter_no_language)
print(counter_english_spanish)
