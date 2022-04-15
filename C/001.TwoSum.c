/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i, j, *ret = malloc(8), sum;
    for (i = numsSize - 1; i >= 0; i--) {
        for (j = 0; j < i ; j++) {
            sum = nums[i] + nums[j];
            if (sum == target) {
                ret[0] = j;
                ret[1] = i;
                return ret;
            }
            else if (sum > target) continue;
        }
    }
    return ret;
}
