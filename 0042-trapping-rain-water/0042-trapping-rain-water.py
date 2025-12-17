class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        l_max,r_max,total=0,0,0
        while(left<=right):
            if (height[left]<=height[right]):
                if(l_max>height[left]):
                    total+=(l_max-height[left])
                else:
                    l_max=height[left]
                left+=1
            else:
                if(r_max>height[right]):
                    total+=(r_max-height[right])
                else:
                    r_max=height[right]
                right-=1
        return total