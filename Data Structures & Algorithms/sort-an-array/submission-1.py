class Solution:

    def merge(self, arr, l, mid, r):
        i, j = l, mid + 1
        help = []

        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                help.append(arr[i])
                i += 1
            else:
                help.append(arr[j])
                j += 1

        while i <= mid:
            help.append(arr[i])
            i += 1

        while j <= r:
            help.append(arr[j])
            j += 1

        for num in help:
            arr[l] = num
            l += 1


    def mergeSort(self,arr,l,r):
        if l == r:
            return arr

        #divide and conquer
        mid = (l + r) // 2
        #recursively sort left half
        self.mergeSort(arr,l,mid)    
        #recursively sort right half
        self.mergeSort(arr,mid+1,r)    

        #merge
        self.merge(arr,l,mid,r)
        return arr


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums,0,len(nums)-1)


        
        