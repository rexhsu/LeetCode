double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int totalSize = nums1Size + nums2Size;
    int *arr = (int *)malloc(totalSize * 4);
    while (nums1Size || nums2Size) {
            if (!nums1Size) {
                        arr[nums2Size - 1] = nums2[nums2Size-1];
                        nums2Size--;
                    }
            else if (!nums2Size) {
                        arr[nums1Size - 1] = nums1[nums1Size-1];
                        nums1Size--;
                    }
            else if (nums1Size && nums2Size) {
                        if (nums2[nums2Size-1] > nums1[nums1Size-1]) {
                                        arr[nums1Size + nums2Size - 1] = nums2[nums2Size-1];
                                        nums2Size--;
                                    } else {
                                                    arr[nums1Size + nums2Size - 1] = nums1[nums1Size-1];
                                                    nums1Size--;
                                                }
                    }
        }
    if (totalSize % 2)
        return (double)(arr[totalSize/2]);
    else
        return (double)(arr[totalSize/2-1] + arr[totalSize/2])/2;
}
