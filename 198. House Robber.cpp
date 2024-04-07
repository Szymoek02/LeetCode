class Solution {
public:
    int rob(vector<int>& nums)
    {
        if(nums.size() < 2)
            return nums[0];

        int a = 0;
        int b = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            int temp = max(a + nums[i], b);
            a = b;
            b = temp;
        }
        return b;
    }
};
