class Solution {
public:
    int robHelper(vector<int>& nums, int start, int n)
    {
        if(n == 1)
            return nums[0];

        int a = 0, b = 0;
        for(int i = start; i < n; i++)
        {
            int temp = max(a + nums[i], b);
            a = b;
            b = temp;
        }

        return b;
    }

    int rob(vector<int>& nums)
    {
        int n = nums.size();

        int skippedFirst = robHelper(nums, 1, n);
        int skippedLast = robHelper(nums, 0, n - 1);

        return max(skippedFirst, skippedLast);
    }
};
