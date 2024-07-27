class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dictionary = collections.defaultdict(list)
        answer = []
        for idx,i in enumerate(groupSizes):
            dictionary[i].append(idx)

        for key, lst in dictionary.items():
            for idx in range(0, len(lst), key):
                answer.append(lst[idx:idx + key])
        return (answer)	