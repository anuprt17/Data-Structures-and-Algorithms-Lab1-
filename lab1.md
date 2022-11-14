# Reflection for Lab 1

1) What did you like/not like about Python?

-->Python's simple syntax has made it my new favourite programming language.  I like python language as it is not  complicated.  Python, especially when compared to C++, is straightforward to learn and implement for me. Python codes are substantially faster to write and execute than other programming languages because they are easy to understand and use. I'm writing code in the Python programming language for the first time, but I didn't find it difficult because of its straightforward syntax.

Well one thing that I would say I need to keep in mind while writing codes in python is "indentation". The spaces at the beginning of a code line are referred to as indentation. Whereas indentation in code is just for readability in other programming languages, it is critical in Python. Python use indentation to denote a block of code. Though, it is good that we no more need the brackets but however as I am new to this language I end up getting run time errors because of indentation.

2) Was there anything that behaved differently than you expected in Python?

-->Python is interesting. There is, however, a lot to learn and practice. The "is" and "==" operators were the ones in Python that performed differently than I expected. I expected both of these operators to provide the same result, but they did not. In this lab, for example, in function sum_to_goal: 

 if list[i] + list[j] == goal:

 if list[i] + list[j] is goal:

Above two are different.  The == operator compares two values by looking for equality. The is operator, on the other hand, compares identities. If two variables point to the same object, an "is" operator evaluates to True. If the objects referred to by the variables are equal, a "==" expression evaluates to True (have the same contents).

3) Based on what you wrote in your lab, write something about the similarities and differences between Python with C/C++ and how that affects how you write your program.

-->C++ code is more complicated than Python code. Python, on the other hand, is easier to code in. For instance, consider the following C++ hello world programme:

#include < iostream> 

using namespace std;

int main()
{
    cout<<"Hello World!";

    return 0;
}


output:
Hello World!

Here's a Python version of the same hello world programme:

Print(“Hello World!”)

In C++, variables are declared. Python does not have a declaration. C++ The programming language is statically typed, which implies that variable declaration, data type of variables, and so on are required. Before utilising a variable in C++, it must be declared by declaring the variable type and variable name. Python is a dynamically typed, therefore variables declaration is not required before using it.

Python is slower than C++ because, unlike C/C++, Python code is interpreted at runtime rather than compiling to native code at build time. 

The C++ function takes a predefined kind of value and returns it. For instance, if a function is called to subtract two integer values, it will only accept integer values as input and produce an integer value as the output. Whereas, the type of the argument and the type of its return value are not constrained in Python.

The allocation of memory to new variables and the deallocation of memory from the variable when it is no longer needed is must in C++ to have effective memory management; otherwise, memory leaks will occur because C++ lacks built-in dynamic memory management.   Python, on the other hand, has the ability to create and deallocate the memory on its own because it contains an internal dynamic memory management system.

Python and C++ have a few things in common, including the fact that both are imperative languages with Object-Oriented programming.
Both languages make use of ASCII characters.
