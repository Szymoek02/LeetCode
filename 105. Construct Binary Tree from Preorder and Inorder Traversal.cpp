/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* construct(vector<int>& preorder, int in_start, int in_end, map<int, int>& mp, int& index)
    {
        if(in_start > in_end) return nullptr;
        TreeNode* root = new TreeNode(preorder[index++]);
        int m = mp[root->val];
        root->left = construct(preorder, in_start, m - 1, mp, index);
        root->right = construct(preorder, m + 1, in_end, mp, index);
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder)
    {
        map<int, int> mp;
        int index = 0;
        for(int i = 0; i < inorder.size(); i++)
            mp[inorder[i]] = i;
        return construct(preorder, 0, inorder.size() - 1, mp, index);
    }
};
