class Solution {
public:
    int maxProduct(vector<int>& nums)
    {
        int n = nums.size();
        int leftProduct = 1;
        int rightProduct = 1;
        int res = nums[0];

        for(int i = 0; i < n; i++)
        {
            leftProduct = (leftProduct == 0) ? 1 : leftProduct;
            rightProduct = (rightProduct == 0) ? 1 : rightProduct;

            leftProduct *= nums[i];
            rightProduct *= nums[n - i - 1];

            res = max(res, max(leftProduct, rightProduct));
        }
        
        return res;
    }
};
