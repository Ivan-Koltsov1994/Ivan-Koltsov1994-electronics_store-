from scr.keyboard import KeyBoard


def test_keyboard_init():
    """Тестируем инициализацию и методы класса Keyboard и Mixinlog"""
    kb = KeyBoard('Logitech G810', 15000, 5)
    assert kb.name == "Logitech G810"
    assert kb.language == "EN"


def test_keyboard_change_yes():
    """Тестируем изменения раскладки клавиатуры методом change_lang в Mixinlog"""
    kb = KeyBoard('Logitech G810', 15000, 5)
    kb.change_lang()
    assert kb.language == "RU"


def test_keyboard_change_no():
    """Тестируем изменения раскладки клавиатуры методом change_lang в Mixinlog"""
    kb = KeyBoard('Logitech G810', 15000, 5)
    kb.change_lang()
    kb.change_lang()
    assert kb.language == "EN"
