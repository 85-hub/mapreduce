class Reducer:
    def reduce(self, shuffleDict):
        for dict_word in shuffleDict:
            sum = 0
            for partialCount in shuffleDict[dict_word]:
                sum += partialCount[1]

                shuffleDict[dict_word] = sum
        return shuffleDict