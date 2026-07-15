class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0, res = 0;
        for(int i=0; i<=nums.length-1; i++){
            if(nums[i] == 0){
                res = Math.max(res, count);
                count = 0;
            }else if(nums[i] == 1){
                count++;
            }
        }
        return Math.max(count, res);
    }
}