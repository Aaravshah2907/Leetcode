class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dic = {}
        for word in strs:
            sortedStr = "".join(sorted(word))
            if sortedStr in ana_dic:
                ana_dic.get(sortedStr).append(word)
            else:
                ana_dic[sortedStr] = [word]
        return [ana_dic[x] for x in ana_dic]