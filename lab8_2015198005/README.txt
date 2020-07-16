Lab 8 answers by Huh Jinwook, student ID 2015198005

Answer Q1 (a): print: 11, 20
               explanation: Function foo() directly multiplies the global variable n by 2.
                            However, foo1() mutates the given parameter and increases it by 1.
                            The 'n' in the definition of foo1() is just a reference to the input parameter and
                            is not related to the global variable n.

Answer Q1 (b): print: 2
               explanation: Function foo() is a gloabl function and function bar() is a local function defined
                            inside foo().
                            Global variable x is initialized as 0.
                            When function foo() is called it first mutates x to 1.
                            Then it calls the local function bar().
                            bar() creates a local variable y and is assigned x + 1, which is 2
                            Finally bar() prints y.

Answer Q1 (c): print: 1
               explanation: Function foo() is identical to question(b)'s function except that foo()
                            does not mutate the global variable x.
                            foo() simply calls the local function bar() and because x remains 0, y=1.
                            Therefore, bar() prints 1.