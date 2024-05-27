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
    TreeNode* construct(vector<int>& preorder, vector<int>& postorder, int& preorder_idx, int& postorder_idx) {
        if(preorder_idx >= preorder.size() || postorder_idx >= postorder.size())
            return nullptr;

        TreeNode* root = new TreeNode(preorder[preorder_idx++]);
        
        if(root->val != postorder[postorder_idx])
            root->left = construct(preorder, postorder, preorder_idx, postorder_idx);

        if(root->val != postorder[postorder_idx])
            root->right = construct(preorder, postorder, preorder_idx, postorder_idx);

        postorder_idx++;
        return root;
    }

    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        int preorder_idx = 0, postorder_idx = 0;
        return construct(preorder, postorder, preorder_idx, postorder_idx);
    }
};
