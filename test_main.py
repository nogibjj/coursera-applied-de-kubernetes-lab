"""
Test goes here

"""

from logic.fruit import get_fruit
from logic.add import adder


def test_adder():
    assert 2 == adder(1, 1)


def test_fruit():
    """Test the fruit function"""
    assert get_fruit() in [
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