# LFA-Limbaje Finite si Automate

## Base info
A project about [LFA](https://www.geeksforgeeks.org/introduction-of-finite-automata/) where I have solved the next tasks:
- Checking if a word is accepted or not by a given DFA / NFA: [AFD.py](AFD.py), [AFN.py](AFN.py);
- Generating all the accepted words for a given finite automata(DFA / NFA / Lambda-NFA): [ALL_WORDS.py](ALL_WORDS.py);
- Converting a Lambda-NFA to a DFA.

The [main.py](main.py) file has all the tasks solved, the previous files are just the separated code for each problem.

## The input format

For every input file, the format is the same.

>[!NOTE]
>For Lambda-NFAs, *l* means *lambda*.

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

