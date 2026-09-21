class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        sorted_items=sorted(freq.items(),key=lambda item:item[1],reverse=True)
        top_k=[item[0] for item in sorted_items[:k]]
        return top_k
        


            





                    
        