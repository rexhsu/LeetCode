int* twoSum(int* nums, int numsSize, int target) {
    int i, j, *ret = malloc(8);
    for (i = numsSize - 1; i >= 0; i--) {
            for (j = 0; j < i ; j++) {
                        if (nums[i] + nums[j] ==  target) {
                                        ret[0] = j;
                                        ret[1] = i;
                                        return ret;
                                    }
                    }
                }
        return ret;
}
