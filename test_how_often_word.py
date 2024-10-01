"""
Test Notes instance method how_often_word()
File: test_how_often_word.py
Developer: Nalin
Collaborator(s): None
"""
import pytest
from notes import Notes


def test_how_often_word_without_repetion():
    """
    Test a sentence that has words without repetition
    """
    sentence = "Test Notes object with"
    actual = Notes.how_often_word(sentence)
    expected = {'Test': 1, 'Notes': 1, 'object': 1, 'with': 1}
    assert actual == expected


def test_hoe_often_word_empty_string():
    """
    Test a sentence that is an empty string
    """
    sentence = ""
    actual = Notes.how_often_word(sentence)
    expected = {}
    assert actual == expected


pytest.main()
