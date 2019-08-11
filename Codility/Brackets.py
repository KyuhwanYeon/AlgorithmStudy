# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:50:45 2019

@author: Kyuhwan
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

#%%

A= '}{[()()]}{'

def reverseBracket(In):
    if In =='{':
        return '}'
    elif In =='[':
        return ']'    
    elif In =='(':
        return ')'    
    elif In =='}':
        return '{'
    elif In ==']':
        return '['    
    elif In ==')':
        return '('      
        
def PositiveOrNegative(In):    
    if (In == '(' )or (In == '{') or (In == '['):
        return 1;
    else:
        return -1;
    #%%

def solution(S):
    if len(S)%2 ==1:
        return 0;
    LeftS = S[:int(len(S)/2)]
    RightS = S[int(len(S)/2):]
    PreSign = 1;
    for idx,v in enumerate(LeftS):
        if idx == 0:
            if PositiveOrNegative(v) == -1:
                return 0;
            
        
        CurSign = PositiveOrNegative(v)
    #    if CurSign !=
        PreSign = PositiveOrNegative(v)
        if reverseBracket(RightS[-(idx+1)]) == v:
            continue;
        else:
            return 0;
    return 1;

#%%
solution(A)