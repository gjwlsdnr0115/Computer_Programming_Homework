Lab 7 answers by Huh Jinwook, student ID 2015198005

Answer Q1: (b), (c), (d)

Answer Q2 (a): proper
Answer Q2 (b): improper, argument a is not an integer
Answer Q2 (c): improper, arguments do not fulfill the requirement n1 <= n2
Answer Q2 (d): proper
Answer Q2 (e): improper, arguments in the function call gcd(c, b) do not fulfill the requirement n1 <= n2

Answer Q3: Output: True
           Explanation: First, l3 is appended into l1 resulting in l1 = [1, 2, ['foo']].
                        Then, l2[0] is assigned with l3 resulting in l2 = [['foo'], 5].
                        Function id() returns the memory location of the passed value.
                        Since both l1[2] and l2[0] originate from the same source, which is l3
                        their memory location is identical.
                        Therefore, print(id(l2[0]) == id(l1[2])) will return True.