def reverse_value_pairs(nums):
    def merge(nums1,nums2):
        p1 =0;p2=0;
        out = []
        rev = 0
        while len(out)<len(nums1)+len(nums2):
            if p1 == len(nums1):
                out.append(nums2[p2])
                p2+=1
            elif p2 == len(nums2) or nums1[p1]<nums2[p2]:
                rev += p2
                out.append(nums1[p1])
                p1 += 1
            elif nums1[p1]>=nums2[p2]:
                out.append(nums2[p2])
                p2 += 1
        return out,rev

    def helper(nums):
        if len(nums)<=1:
            return nums,0
        mid = len(nums)//2
        left,sortl = helper(nums[:mid])
        right,sortr = helper(nums[mid:])
        out,rev = merge(left,right)
        return out,rev+sortl+sortr
    return helper(nums)

if __name__ == '__main__':
    out,sorta = reverse_value_pairs([7,5,6,4])
    print(out)
    print(sorta)