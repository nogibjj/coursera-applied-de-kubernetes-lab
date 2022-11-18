from random import choices


def get_fruit():
    """Get a random fruit from a list of fruits"""

    fruits = [
        "apple",
        "banana",
        "cherry",
        "durian",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "jackfruit",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "pear",
        "quince",
        "raspberry",
        "strawberry",
        "tomato",
        "watermelon",
    ]
    return choices(fruits)[0]
