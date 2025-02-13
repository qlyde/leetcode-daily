class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)
        def merge(l, r):
            merged = []
            i, j = 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    merged.append(l[i])
                    i += 1
                else:
                    merged.append(r[j])
                    j += 1
            merged.extend(l[i:])
            merged.extend(r[j:])
            return merged

        def mergeSort(a):
            if len(a) <= 1:
                return a

            m = len(a) // 2
            l = mergeSort(a[:m])
            r = mergeSort(a[m:])
            return merge(l, r)

        return mergeSort(nums)
        