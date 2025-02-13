class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##### Heap Solution #####
        # # Time: O(n + klogn)
        # # Space: O(n)
        # c = defaultdict(int)
        # for num in nums:
        #     c[num] += 1

        # h = [(-v, k) for k, v in c.items()]
        # heapify(h)
        # res = []
        # for _ in range(k):
        #     _, elem = heappop(h)
        #     res.append(elem)
        # return res

        ##### Bucket Sort Solution #####
        # Time: O(n)
        # Space: O(n)
        freqs = [[] for _ in range(len(nums) + 1)]
        c = defaultdict(int)
        for num in nums:
            c[num] += 1
        for num, cnt in c.items():
            freqs[cnt].append(num)
        res = []
        for i in range(len(freqs) - 1, -1, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    break
            else:
                continue
            break
        return res
