class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int max_area = 0;
        while(i < j)
        {
            max_area = std::max(max_area, std::min(height[j], height[i]) * (j - i));
            if(height[i] < height[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return max_area;
    }
};