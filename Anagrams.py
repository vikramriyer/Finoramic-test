class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        
        A = list(A)
        if len(A) == 
        h = {}
        for i, word in enumerate(A):
            word = [x for x in word]
            word.sort()
            A[i] = ''.join(word)

        for i, word in enumerate(A):
            if word in h:
                h[word].append(i+1)
            else:
                h[word] = [i+1]

        return list(h.values())
