import random

A_cities = ['Абакан', 'Азов', 'Александров', 'Алексин', 'Альметьевск', 'Анапа', 'Ангарск', 'Анжеро-Судженск', 'Апатиты',
            'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск', 'Асбест', 'Астрахань', 'Ачинск']
B_cities = ['Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Барнаул', 'Батайск', 'Белгород', 'Белебей', 'Белово',
            'Белогорск', 'Белорецк', 'Белореченск', 'Бердск', 'Березники', 'Березовский', 'Бийск', 'Биробиджан',
            'Благовещенск', 'Бор', 'Борисоглебск', 'Боровичи', 'Братск', 'Брянск', 'Бугульма', 'Буденновск', 'Бузулук',
            'Буйнакск']

all_cities = []
all_cities.extend(A_cities)
all_cities.extend(B_cities)
start = random.choice(all_cities)
inp = str(input())
end_symbol = (inp[-1::])
print(end_symbol)
while inp not in all_cities:
    print('Нужно ввести название города!')
    inp = str(input())