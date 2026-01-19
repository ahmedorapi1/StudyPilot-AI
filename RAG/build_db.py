from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

theory = [
"""
Derivatives are a fundamental concept in calculus. A derivative represents the rate of change of a function with respect to a variable. 
For example, if f(x) = x^2, then the derivative f'(x) = 2x. 
This means that the function x^2 is increasing faster as x becomes larger.

The derivative is used in many real-life applications such as physics, engineering, and economics. 
In physics, derivatives describe velocity as the rate of change of position, and acceleration as the rate of change of velocity.
In economics, derivatives can describe how cost or profit changes with production.

Basic derivative rules include:
- The derivative of x^n is n*x^(n-1)
- The derivative of a constant is zero.
- The derivative of a sum of functions is the sum of their derivatives.
""",

"""
Quadratic equations are algebraic equations of the form ax^2 + bx + c = 0, where a ≠ 0.
They can be solved using several methods, including factorization, completing the square, and the quadratic formula.

The quadratic formula is:
x = (-b ± √(b^2 - 4ac)) / (2a)

The expression inside the square root, b^2 - 4ac, is called the discriminant.
If the discriminant is positive, the equation has two real solutions.
If it is zero, the equation has one real solution.
If it is negative, the equation has no real (but two complex) solutions.
""",

"""
The square root of a number is a value that, when multiplied by itself, gives the original number.
For example, the square root of 64 is 8, because 8 × 8 = 64.

Square roots are used in geometry, trigonometry, and many engineering calculations.
Not all numbers have real square roots. For example, the square root of -1 is not a real number.

In mathematics, square roots are written using the radical symbol √.
"""
]
questions = [
"""
1) Find the derivative of the function f(x) = x^2.
2) Differentiate the function f(x) = 3x^3.
3) What is the derivative of f(x) = 5x?
4) Find f'(x) if f(x) = x^4.
5) Differentiate: f(x) = 2x^2 + 3x.
""",

"""
6) Solve the quadratic equation: x^2 - 5x + 6 = 0.
7) Find the roots of: x^2 + 7x + 10 = 0.
8) Using the quadratic formula, solve: 2x^2 - 4x - 6 = 0.
9) What is the discriminant of: x^2 + 4x + 4 = 0?
10) How many real solutions does the equation x^2 + 1 = 0 have?
""",

"""
11) Find the square root of 49.
12) What is √81?
13) Find √16.
14) What is the square root of 121?
15) Is √(-9) a real number? Explain.
"""
]


splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

document_theory = splitter.create_documents(theory)
document_questions = splitter.create_documents(theory)


emd = OllamaEmbeddings(model="nomic-embed-text")

_ = Chroma.from_documents(document_theory, emd, persist_directory="theory_db")
_ = Chroma.from_documents(document_questions, emd, persist_directory="questions_db")
