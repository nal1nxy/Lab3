- **Developer**: Nalin
- **Collaborator(s)**: None

## size() method design
To find out how many elements in the `self.notes` list, we use the Python built-in 
function `len()`.
- Call `len()` with argument `self.notes` and return the result. 

## how_often_word() method design
- Define a method `how_often_word()` with one parameter.
- The parameter of the method is `sentence` of the data type `string`.
- Define an accumulator variable `my_dict`.
- Assign an empty dictionary to the accumulator variable `my_dict`.
- Define a variable `my_list`.
- Use the `split()` method on the parameter `sentence`  and assign it to the variable `my_list`.
- Use `for loop` with iterator variable as `word` to iterate through the following:
    - Use `get()` method on the accumulator variable(dictionary) to get the value of `word` and increment it by 1.
    - assign the above to the value of `word` as key to the dictionary `my_dict`.
- Return `my_dict`.

## wprd_histogram() method design
- Define a method `word_histogram()` with one parameter.
- The parameter of the method is `self` of the datatype instance of the class `Notes`.
- Define a variable `sentence_of list`.
- Join the items in the list `self.notes`(instance variable of the class `Notes`) with a string containing just a blank space as athe delimiter and assign it to the variable `sentence_of_list`.
- Pass the list `sentence_of_list` as the parameter to the static method `how_often_word()` by calling it through the class `Notes` and return it.