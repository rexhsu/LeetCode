class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        // sort
        sort(nums.begin(), nums.end());
        
        int sol = 0;
        int i = 0;
        int j = nums.size() - 1;
        while (i<j) {
            if (nums[i] + nums[j] > k) {
                j--;
            } else if (nums[i] + nums[j] < k) {
                i++;
            } else {
                sol++;
                i++;
                j--;
            }
        }
        return sol;
    }
};