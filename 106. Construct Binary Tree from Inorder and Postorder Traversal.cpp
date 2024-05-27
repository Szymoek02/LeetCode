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
    unordered_map<int, int> inorder_map;
    TreeNode* construct(int in_start, int in_end, vector<int>& postorder, int& post_idx)
    {
        if(in_start > in_end) // !!!
            return nullptr;
        TreeNode* root = new TreeNode(postorder[post_idx--]);

        int inorder_index = inorder_map[root->val];
        root->right = construct(inorder_index + 1, in_end, postorder, post_idx);
        root->left = construct(in_start, inorder_index - 1, postorder, post_idx);
        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int post_idx = postorder.size() - 1;
        int in_size = inorder.size();

        for(int i = 0; i < in_size; i++)
            inorder_map[inorder[i]] = i; 
        
        return construct(0, in_size - 1, postorder, post_idx);
    }
};
