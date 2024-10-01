"""
Test Notes instance method word_histogram()
File: test_word_histogram.py
Developer: Nalin
Collaborator(s): None
"""
import pytest
from notes import Notes


def word_histogram_empty_strings():
    """
    Test a list of empty strings
    """
    notes = ["", "", "", ""]
    n_obj = Notes(notes)
    actual = n_obj.word_histogram()
    expected = {}
    assert actual == expected


def word_histogram__repetitive_words():
    """
    Test a list of repetitive strings
    """
    notes = ["notes", "is", "back", "back", "notes"]
    n_obj = Notes(notes)
    actual = n_obj.word_histogram()
    expected = {'notes': 2, 'is': 1, 'back': 2}
    assert actual == expected


pytest.main()
