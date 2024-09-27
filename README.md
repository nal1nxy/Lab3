> **COMP-801 Integrated Computing Practice**
# Lab 3

## Due Dates
- Assigned Week 5
- Due before midnight before Week 6 class

## Requirements
- Complete AR5. Give special attention to Ch 11 Dictionaries.
- Develop two instance methods in the class `Notes`
- Use test-driven incremental development to
  - document the modules and `DESIGN.md`
  - write test cases for the methods
  - design how the methods should be implemented
  - implement the methods.
- Apply version control to demonstrate the development steps. 

## Getting Started
Follow the steps used in previous labs and homework to:
1. Clone the remote repo in your `comp801/labs` directory with appropriate `git` command in a `bash` terminal
2. Open **lab3** in VS Code
  - Read the code in all three Python modules: `notes.py`,  `client.py`, and `test_size.py`
  - Run all three modules and fix errors and **Problems** reported by VS Code, if any
3. Create testing modules for the methods in `Notes` class except for `size()` method
4. Check and fix the errors reported in VS Code **Problems** panel.

## Evaluation
#### Documentation, 10 pts
- It's all or nothing
  - Full credit, 10 pts, if nothing is missing
  - No credit otherwise.

In each file (`.py` and `DESIGN.md`) enter your name and your collaborator(s) names. 

### Testing, 20 pts
- 1 testing module for EACH method in the `Notes` class
- 2 testing functions in each testing module. 

Note that `size()` method already has its testing module with two testing functions as examples. 

### DESIGN.md, 20 pts
- 1 design for each `Notes` method, 10 pts each

Note that `size()` method already has the design as an example. 

### Implementation, 20 pts
- 2 `Notes` methods, 10 pts each
- Do NOT use list comprehensions or techniques that are not included in your readings.  

### Incremental development, 20 pts
- 1 initial commit: to document all files developer and collaborator(s) names (2 points)
- 3 commits for the development of each method for a total of 6 commits, 3 points each. 

### Code analysis and styling, 10 pts
Submitted work should be free of **Problems** reported in VS Code. 

## Submission
### GitHub
- Local commit history and and all committed changes are pushed to the remote repository

### Canvas
- Convert `DESIGN.md` to PDF using Microsoft extension available in VS Code, Markdown PDF
- Upload the PDf to the submission link in Canvas.

## Guidelines
These guidelines are aligned with the evaluation criteria above. 

1. **Document** ALL files with developer and collaborator(s) names
  - Version control this step
2. **Understand** what each method is supposed to do, based on the docstring 
   description, BEFORE writing the test cases.
3. Write **testing functions** to demonstrate your understanding of each method.
  - Version control this step.
4. **Design** each method before coding.
  - Version control this setp
5. **Write code** incrementally, one method at a time
  - Version control this step
6. Run the tests, debug and fix errors as you go.
  - Version control this step, if needed.
7. Repeat steps 2 tp 6.
8. **Code analysis and stylinge**: fix all problems.

## Collaboration
Collaboration is allowed.

- Ask questions of your collaborator, CAs, and instructor; 
- Answer questions and give advice to your peers via Discussion posts, during study group, or one-on-one collaborations;  
  - Discuss and clarify concepts
  - Show or practice concepts on simple examples. 

You are NOT allowed to give your work on this assignment to somebody else,
  or to do it for someone else. Collaboration is sharing ideas as they are 
  developed; it is not sharing design descriptions or code. 

