class Solution {
public:
    int count(string s, int l, int r)
    {
        int n = s.length();
        int count = 0;
        while(l >= 0 && r < n && s[l] == s[r])
        {
            l--;
            r++;
            count++;
        }
        return count;
    }

    int countSubstrings(string s) {
        int n = s.length();
        int res = 0;
        for(int i = 0; i < n; i++)
        {
            res += count(s, i, i);
            res += count(s, i ,i + 1);
        }

        return res;
    }
};
