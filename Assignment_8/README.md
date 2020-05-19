In this particular assignment, we tried to stimulate a flight management system at a basic level using Prolog.
So, Prolog(PROgramming LOGic) is a type of declarative programming language. 
I learnt quite a lot of concepts in Prolog and during this assignment like:-
1. Resolution :- In prolog, the derivation of new statements using the previous ones is resolution. It is used by prolog a lot of times internally
when it has to answer some query and it checks the rules and facts.
2. Also in prolog we never actually write a code for a program, we just write a database including facts and rules and prolog itself figures
out the way to answer the queries using this information.
3. Unification :- It is a way in which prolog matches two terms i.e., it associates variables and values. And the variables that recieve a 
value are said to be instantiated. It performs unification using many rules like checking the number of arguments, etc which helps prolog
to find answers by comparison and elimination.
4. Backtracking :- Prolog implements backward chaining i.e., it follows Depth First backtracking for solving a query. It works according to the
conditional AND or OR and uses backtracking helping it to first solve subclauses and go back(redo) if there is a mismatch.
