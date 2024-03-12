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
    TreeNode* construct(vector<int>& preorder, vector<int>& inorder, 
    size_t pre_start, size_t pre_end, size_t in_start, size_t in_end)
    {
        if(pre_start > pre_end || in_start > in_end) return nullptr;
        TreeNode* res = new TreeNode;
        res->val = preorder[pre_start];
        size_t m;
        for(size_t i = 0; i < inorder.size(); i++) {
            if(inorder[i] == preorder[pre_start]) {
                m = i;
                break;
            }
        }

        res->left = construct(preorder, inorder, pre_start + 1, pre_start + m, in_start, );
        res->right = construct(preorder, inorder, pre_start + m + 1, );
        return res;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
        return construct(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1);
    }
};
