class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        n = len(A)
        cur_close = None
        A.sort()
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                sum3 = A[i] + A[j] + A[k]
                if sum3 == B:
                    return sum3
                if cur_close is None or abs(sum3 - B) < abs(cur_close - B):
                    cur_close = sum3
                if sum3 < B:
                    j += 1
                else:
                    k -= 1
        return cur_close
