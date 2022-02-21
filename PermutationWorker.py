class PermutationWorker:
    def __init__(self, string):
        self.string = string
        self.elms = []
        self.cache = {}

        self.buildElements()

    def buildElements(self):
        self.elms = [e for e in self.string]
        
    def generateCombinations(self, length=0):
        return self._generateCombinations(self.elms[:])

    """    
        Basically what I do is to combine each element of my array
        with the combinations of the elements that are after the first element of the array being proccessed.
        
        1 - The first I do in function is validate if the array gotten has just one element,
        if so I return a two dimensional array with that element. Example: [ [1] ].
        This is also my base case.
        2 - Create an combination variable to hold all of the combinatios that are going to be generated at that stack.
        3 - Loop over the array.
        4 - For each pass swap each element with the first element(the one at index 0).
            I do this to avoid having the same number repated in a combination.
        5 - Recursively call the combination function for the elements that are after the first element of the array,
            and allocate the combinations into the variable created at step 0. Example if you have an array=[1, 2, 3],
            so then we will call the combination function for the elements [2, 3].
        6 - Then I combine the first element of my array(the one at index 0) with all the gotten combinations.
        7 - Then I return those combinations
    """    
    def _generateCombinations(self, elms):

        ckey = elms[0] + ':' + elms[len(elms) - 1] + ':' + str(len(elms))

        if ckey in self.cache:
            return self.cache[ckey]
        
        if len(elms) == 1:
            return [elms]

        combinations=[]
        for idx in range(len(elms)):
            elms[0], elms[idx] = elms[idx], elms[0]

            subcombs = self._generateCombinations(elms[1:])

            for subComb in subcombs:
                subComb.append(elms[0])
                combinations.append(subComb)


        self.cache[ckey] = combinations
        
        return combinations
            
if __name__ == '__main__':

    tests = [
        {'input': {'elms': 'abc'}}
    ]

    for test in tests:
        
        pWorker = PermutationWorker(test['input']['elms'])
        result = pWorker.generateCombinations()

        print(result)
        #print('Input: ', test['input'], ', Result: ', result, ', Expected: ', test['expect'], ', Test Passed: ', test['expect'] == result)
      
