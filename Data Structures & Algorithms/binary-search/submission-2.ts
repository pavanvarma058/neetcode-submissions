class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        let low = 0;
        let high = nums.length;
        while (low < high) {
            const mid = Math.floor(low + (high - low) / 2);
            const value = nums[mid];
            if (value === target) {
            return mid;
            } else if (value < target) {
            low = mid + 1;
            } else {
            high = mid;
            }
        }
        return -1;
    }
}
