import random

students = ["Antonelli",
"Alvarez Bibiloni",
"Saluzzi",
"Larrea",
"Fijalkauskas",
"Sobrino",
"Klappenbach",
"Lagares",
"Wolfsohn",
"Orlando",
"Nastri",
"Abeliansky",
"Wolberg",
"Conte Grand",
"Sanguinetti"
]


def make_random_groups(students, number_of_groups):
    # Shuffle list of students
    random.shuffle(students)

    # Create groups
    all_groups = []
    for index in range(number_of_groups):
        group = students[index::number_of_groups]
        all_groups.append(group)

    # Format and display groups
    for index, group in enumerate(all_groups):
        print(f"✨Group {index + 1}✨: {' / '.join(group)}\n")

make_random_groups(students, 5)