"""
Demonstrate functionality of the Paragraph class.
File: src/client.py
Initial developers: COMP 801 instructors
Developer: Nalin
Collaborator(s): None
"""
from notes import Notes


def main():
    """
    Demo Notes functionality
    """
    notes_lst = ['sunny day today!', 'need a break', 'going for a walk']
    n_obj = Notes(notes_lst)
    n_count = n_obj.size()
    print(f'Notes count: {n_count}')

    # create another Notes object and find out something else about it.
    Sentence = "create another Notes object and find out something else about it."
    print(Notes.how_often_word(Sentence))


main()
