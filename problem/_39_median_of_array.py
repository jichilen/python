def median_of_array(nums):
    l = len(nums)
    def helper(nums,bg,ed):
        if ed-bg==0:
            return
        if ed-bg==1:
            return nums[bg]
        fl = bg
        for i in range(bg+1,ed):
            if nums[i]<nums[bg]:
                fl+=1
                nums[i],nums[fl]=nums[fl],nums[i]
        nums[bg],nums[fl]=nums[fl],nums[bg]
        if fl > l//2:
            return helper(nums,bg,fl)
        elif fl == l//2:
            return nums[fl]
        else:
            return helper(nums,fl+1,ed)
    return helper(nums,0,l)




if __name__ == '__main__':
    nums = [1,3,2,2,2,2,4,5,5,5,5,5,2]
    print(median_of_array(nums))