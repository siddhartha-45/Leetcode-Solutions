class Solution {
    public int rob(int[] nums) {
        int i=0;
        int j=0;
        for(int k=0;k<nums.length;k++){
            int curr=Math.max(i,j+nums[k]);
            j=i;
            i=curr;
        }
    return i;
    }
    
}