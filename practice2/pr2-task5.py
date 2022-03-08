from random import randrange


# Function that generates random reports on digital economics
def generate_report():
    # sentence parts pool taken from table in practice .ipynb
    # could as well put it into a json but meh
    data = [
        [
            "Коллеги,",
            "парадигма цифровой экономики",
            "открывает новые возможности для",
            "дальнейшего углубления",
            "знаний и компетенций."
        ],
        [
            "В то же время,",
            "контекст цифровой трансформации",
            "выдвигает новые требования",
            "бюджетного финансирования",
            "непроверенных гипотез."
        ],
        [
            "Однако,",
            "диджитализация бизнес-процессов",
            "несёт в себе риски",
            "синергетического эффекта",
            "волатильных активов."
        ],
        [
            "Тем не менее,",
            "прагматичный подход к цифровым платформам",
            "расширяет горизонты",
            "компрометации конфиденциальных",
            "опасных экспериментов."
        ],
        [
            "Следовательно,",
            "совокупность сквозных технологий",
            "заставляет искать варианты",
            "универсальной коммодитизации",
            "государственно-частных партнёрств."
        ],
        [
            "Соответственно,",
            "программа прорывных исследований",
            "не оставляет шанса для",
            "несанкционированной кастомизации",
            "цифровых следов граждан."
        ],
        [
            "Вместе с тем,",
            "ускорение блокчейн-транзакций",
            "повышает вероятность",
            "нормативного регулирования",
            "нежелательных последствий."
        ],
        [
            "С другой стороны,",
            "экспоненциальный рост Big Data",
            "обостряет проблему",
            "практического применения",
            "внезапных открытий."
        ]
    ]

    sentences = list()

    # generating random sentences
    for i in range(9):
        sentence = ""
        for j in range(5):
            # so that first sentence is a proper opener phrase
            if i == 8:
                k = 0
            else:
                k = randrange(1, 8)
            sentence += data[k][j] + " "
        sentences.append(sentence)

    # printing the generated report
    for i in range(3):
        print(f"{sentences.pop()}{sentences.pop()}{sentences.pop()}")


def main():
    generate_report()


if __name__ == '__main__':
    main()