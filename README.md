# Python Data Structures And Abstractions
---
## Description  
This package currently provides a robust min heap class written in python. Soon, a max heap, and priority queue will be implemented, and further down the road more data structures will be included.

Each of these classes is well tested (tests are included), and their methods are documented with a brief description as well as notes for time and space complexity. Plans for additional features and future improvements are commented in a "*TODO*" note at the top of the classes.

The goal for these classes is to make them convenient, easy to use, and as efficient as can be expected given that they are implemented in python. Additionally, I want the design to be organized and elegant.

The purpose of this project is to help me learn. I am building these data structures and abstractions to get a deeper understanding of how they work and what they can be used for. Once they are built, they will be convenient tools to use for practicing algorithms that leverage them, and enhancing programs that would benefit from them.  

--- 
## How To Use This Package
- Download this zip folder or clone the repository (zip folder not yet included)
- Make sure to extract the contents or clone the repository to a preferred location
- (Currently looking into what else to do. Will involve adding the package to your PATH)

Once the package is added to your path, you should be able to use it in any python file by simply importing it.

(Will add a screenshot here)

---
## Tests
To run the test cases for any of these classes, open the *test_scripts* directory, and type one of the following commands into the terminal. The one that works will depend on whether python is added to your path. Note, if you have both python version 2 and python version 3 installed, you will need to specify *py3*: 
```console
py -m pytest <insert_desired_test_file_name_here.py>
```
Or:
```console
python -m pytest <insert_desired_test_file_name_here.py>
```
Or if your python installation is added to your path correctly, you should be able to simply run:
```console
pytest <insert_desired_test_file_name_here.py>
```
Every class has its own test file, and you can run test_all.py (coming soon) to test the entire package at once.

---
## Dependencies
You will need to download the following to use this project:  
- python version 3 (This was written in 3.11, but it shouldn't make a difference as long as you use version 3)
- pytest
- multipledispatch

---
## Acknowledgements 
Big thanks to Gayle Laakmann McDowell at HackerRank for providing [a very useful resource](https://www.youtube.com/watch?v=t0Cq6tVNRBA) for getting started on this project.

---
## License
[BSD-2-Clause](LICENSE.md)


