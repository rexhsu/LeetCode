bool canJump(int* nums, int numsSize){
    int farest = 0;
    for (int i=0; i<numsSize-1; i++) {
        if (farest < i || farest >= numsSize-1) break;
        if (farest < i+nums[i]) farest = i+nums[i];
    }
    return farest >= (numsSize-1);
}
