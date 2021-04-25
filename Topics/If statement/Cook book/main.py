pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

recipes = (pasta, apple_pie, ratatouille, chocolate_cake, omelette)


def recepie_checker(ingridient):
    output = []
    for recipe in recipes:
        if ingridient in recipe:
            if recipe == pasta:
                output.append('pasta')
            if recipe == apple_pie:
                output.append('apple pie')
            if recipe == ratatouille:
                output.append('ratatouille')
            if recipe == chocolate_cake:
                output.append('chocolate cake')
            if recipe == omelette:
                output.append('omelette')
    for item in output:
        print(f'{item} time!')


val = input()
recepie_checker(val)