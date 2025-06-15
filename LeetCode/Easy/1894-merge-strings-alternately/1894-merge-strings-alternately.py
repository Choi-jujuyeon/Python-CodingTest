class Solution(object):
    def mergeAlternately(self, word1, word2):
        arr=[]
        for i in range(max(len(word1),len(word2))): #길이최대

            arr.append("" if i+1>len(word1) else word1[i] )
            arr.append("" if i+1>len(word2) else word2[i] )
        return "".join(arr)