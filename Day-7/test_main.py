from main import indexes_of_letter_in_word, replace_letter_in_word_at_indexes


def test_indexes_of_letter_in_word():
    assert indexes_of_letter_in_word('a', 'hello') == []
    assert indexes_of_letter_in_word('e', 'hello') == [1]
    assert indexes_of_letter_in_word('l', 'hello') == [2, 3]
    
    
def test_replace_letter_in_word_at_indexes():
    assert replace_letter_in_word_at_indexes('hello', '1', [2, 3]) == 'he11o'
    assert replace_letter_in_word_at_indexes('a', 'e', [0]) == 'e'
    assert replace_letter_in_word_at_indexes('Good morning', 'h', [0, 3, 11]) == 'hooh morninh'