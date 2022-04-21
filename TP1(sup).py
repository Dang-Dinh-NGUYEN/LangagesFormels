# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:57:08 2022

@author: Dang Dinh NGUYEN
"""

import os
import time
EPSILON = "&"

########################################################################
########################################################################

class FileHandler:

    def __init__(self):
        pass

    def readFile(self, filePath):
        lines=[]
        if(os.path.isfile(filePath)):
            try:
                with open(filePath) as file:
                    lines = [line.rstrip() for line in file]
            except IOError as e:
                print("File could not be opened.")
                exit(0)
        else:
            print('{} :File was not found in the specified path.'.format(filePath))
            exit(0)
        return lines

    def parseFile(self,lines):
        ''' Line 1: Total States
            Line 2: Input Word Symbols
            Line 3: Stack Symbols
            Line 4: List of Final States
            Line 5 to end: Transitions in form of
                    (Current State, Current Input Symbol, Current Top of Stack, Next State, Push/Pop Operation Symbol)
            '''
        states = lines[0].rstrip().split()
        input_symbols = lines[1].rstrip().split()
        stack_symbols = lines[2].rstrip().split()
        final_states = lines[3].rstrip().split()
        transitions = lines[4:]
        for i in range(len(transitions)):
            transitions[i] = transitions[i].rstrip().split()

        parsedLines = { 'states':states,
                        'input_symbols':input_symbols,
                        'stack_symbols':stack_symbols,
                        'final_states':final_states,
                        'transitions':transitions}
        return parsedLines

class PDA:
    def __init__(self):
        self.stack = []
        
    def computing(self, inputString, parsedLines):
        inputString += "&"
        initStackSymbol = "Z"
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        stackSymbols = parsedLines['stack_symbols']
        transitions = parsedLines['transitions']
        initState = "1"
        
        currentStackSymbol = "Z"
        currentState = initState
        
        #print('State\tSymbol\tStack\tTransition')
        print('{}\t {}\t {}\t {}\t'.format(currentState,'_',currentStackSymbol,self.stack))
        
        for char in inputString:
            found = False
            for transition in transitions:
                if((currentState == transition[0] and char == transition[1]) and currentStackSymbol == transition[2]):
                    currentState = transition[3]
                    found = True
                    if(len(transition[4]) == 2): 
                        self.stack.append(transition[4][0])
                    elif(len(transition[4]) == 2):
                        self.stack.append(transition[4][-1])
                        self.stack.append(transition[4][-2])
                    elif(transition[4] == "&" and len(self.stack) != 1):
                        self.stack.pop()
                        break
            if found == True:   
                previousStackSymbol = currentStackSymbol
                currentStackSymbol = self.stack[len(self.stack)-1]
                print('{}\t {}\t {}\t ({}, {})'.format(currentState, char, previousStackSymbol, currentStackSymbol, self.stack))
            else:
                print("NO")
                return
        if currentState in finalStates:
            print("YES")
        else:
            print("NO")
            
def main():
    
    fh = FileHandler()
    pda = PDA()
    automataFilePath = input('Enter the automata file path: ')
    lines = fh.readFile(automataFilePath)
    
    inputString = input('Enter input String: ')
    inputString = inputString.rstrip()
    
    parsedLines = fh.parseFile(lines)
    print('States: ', parsedLines['states'])
    print('Input Symbols: ', parsedLines['input_symbols'])
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    print('Initial Stack Symbol: ', "Z")
    print('Final States: ', parsedLines['final_states'])
    print('Transitions List:')
    for production in parsedLines['transitions']:
        print('\t', production)
    #time.sleep(2)
    print('Details loaded')
    print('Computing the Transition Table:')
    pda.computing(inputString, parsedLines)

if __name__ == '__main__':
    main()
                    
                        
                
        
        
        
        
        