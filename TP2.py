# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:20:19 2022

@author: Dang Dinh NGUYEN
"""

import os
import time
from tabulate import tabulate
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
        ''' 
            Line 1 to end: Productions in form of
                    (Current State -> Next State)
        '''
        productions = lines[0:]
        for i in range(len(productions)):
            productions[i] = productions[i].rstrip().split('->')

        parsedLines = {'productions':productions}
        return parsedLines
    
class CYK:
    def __init__(self):
        pass
    
    def isRecognised(self, inputString, parsedLines):
        n = len(inputString)
        productions  = parsedLines['productions']
        source = productions[1][0]
        print("source ", source)
        table =  [[set([]) for i in range(n)] for j in range(n)] 
        
        for j in range(0,n):
            for production in productions:
                lhs = production[0]
                rhs = production[1]
                #print('{}\t {}'.format(lhs, rhs))
                if (len(rhs) == 1 and rhs.islower()) and rhs == inputString[j]:
                    table[j][j].add(lhs)
            
            for i in range(j,-1,-1):
                for k in range(i,j+1):
                    for production in productions:
                        lhs = production[0]
                        rhs = production[1]                    
                        try:
                            if (len(rhs) == 2) and (rhs[0] in table[i][k]) and (rhs[1] in table[k + 1][j]):
                                table[i][j].add(lhs)
                        except:
                            pass
                                
        if len(table[0][n-1]) != 0 and source in table[0][n-1] :
            print("True")
        else:
            print("False")
        
            
        for i in range(1,n):
                table[i] = sorted(table[i],reverse = True)
                    
        result = []
        for i in range(0,n):
            l = []
            for j in range(0,n):
                    l.append(list(table[j][i]))
            result.append(l)
            
        headers = (list(inputString))
        print('')
        print(tabulate(result,headers,tablefmt = "orgtbl"))
        print('')
     
    
def main():
    
    fh = FileHandler()
    cyk = CYK()
    FilePath = input('Enter the automata file path: ')
    lines = fh.readFile(FilePath)
    
    inputString = input('Enter input String: ')
    inputString = inputString.rstrip()
    
    parsedLines = fh.parseFile(lines)
    print('Productions List:')
    for production in parsedLines['productions']:
        print('\t', production)
    #time.sleep(2)
    print('Details loaded')
    cyk.isRecognised(inputString, parsedLines)
   

if __name__ == '__main__':
    main()
                    