class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums1의 마지막 인덱스값 체크
        last = m+ n-1

        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]= nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last-=1

        # nums1은 다 0이라 위 조건에 안 걸릴 경우
        # num2에 값이 남아 있는 경우
        while n>0:
            nums1[last] = nums2[n-1]
            n,last = n-1, last -1