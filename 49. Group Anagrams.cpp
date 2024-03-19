class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> mp;
        for(auto& str: strs)
        {
            string word = str;
            std::sort(str.begin(), str.end());
            mp[str].push_back(word);
        }

        for (auto it = mp.begin(); it != mp.end(); ++it)
        {
            vector<string> group;
            for(auto i: it->second)
            {
                group.push_back(i);
            }
            res.push_back(group);
        }

        return res;
    }
};
