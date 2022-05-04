class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        vector<int> fnums(nums.size());
        copy_if(nums.begin(), nums.end(), fnums.begin(), [=](int em) {
            return (em<k);
        });
        
        // sort
        sort(fnums.begin(), fnums.end());
        /* debug
        for_each(fnums.begin(), fnums.end(),
                  [](const int& n) { cout << n << " "; });
        cout << endl;
        */

        int sol = 0;
        int i = 0;
        int j = fnums.size() - 1;
        while (i<j) {
            if (fnums[j] > k or fnums[i] + fnums[j] > k) {
                j--;
            } else if (fnums[i] + fnums[j] < k) {
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