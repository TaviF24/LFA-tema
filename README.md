# LFA-Limbaje Finite si Automate

## Base info
A project about [LFA](https://www.geeksforgeeks.org/introduction-of-finite-automata/) where I have solved the next tasks:
- Checking if a word is accepted or not by a given DFA / NFA: [AFD.py](AFD.py), [AFN.py](AFN.py);
- Generating all the accepted words for a given finite automata(DFA / NFA / Lambda-NFA): [ALL_WORDS.py](ALL_WORDS.py);
- Converting a Lambda-NFA to a DFA.

The [main.py](main.py) file has all the tasks solved, the previous files are just the separated code for each problem.

## The input format

For every input file, the format is the same.

```
q0          //the starting state
q1 q3       //the final states
q0 1 q0     //the current state - the symbol - the next state  
q0 0 q1
q1 1 q0
q1 0 q2
q2 2 q3     
```
The above input looks like this:

<img width="592" alt="Screenshot 2023-09-02 at 18 26 47" src="https://github.com/TaviF24/LFA-project/assets/118764142/d92b0eb5-b15f-43bf-b054-ba99efb9c1b3">


>[!NOTE]
>You can use any characters for the states and symbols, except the '**l**' character.
>For Lambda-NFAs, '**l**' means *lambda*.


```
q0          //the starting state
q4          //the final states
q0 + q1     //the current state - the symbol - the next state  
q0 l q2
q1 4 q2
q2 0 q3
q3 2 q4
q3 3 q4
q3 7 q4   
```
The above input looks like this:

<img width="498" alt="Screenshot 2023-09-02 at 18 40 43" src="https://github.com/TaviF24/LFA-project/assets/118764142/827f6ad9-ad94-46f2-9acf-b7e97077dab9">

## The output

The result of ```Converting a Lambda-NFA to a DFA``` will be in the [output_converter.txt](output_converter.txt) file, with the same format as the input.

>[!NOTE]
>The new states are created by concatenating old states.

## What I used
- Operating system: MacOS
- Language: Python 3.10
- IDE: PyCharm 2022.2.5




