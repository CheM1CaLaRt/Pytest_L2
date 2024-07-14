import pytest
from my_module import count_vowels  # Предполагаем, что функция находится в модуле my_module.py

def test_all_vowels():
    assert count_vowels("aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ") == 30

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
    assert count_vowels("бвгджзйклмнпрстфхцчшщ") == 0

@pytest.mark.parametrize("s, expected", [
   ("Hello World!", 3),
   ("PyThOn", 1),
   ("Привет Мир!", 3),
   ("12345AEIOUаеёиоуыэюя67890", 15),
])
def test_is_chars(s, expected):
   assert count_vowels(s) == expected


if __name__ == "__main__":
    pytest.main()
