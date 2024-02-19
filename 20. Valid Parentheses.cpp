class Solution {
public:
    bool isValid(string s) {
        if(s[0] == ')' || s[0] == '}' || s[0] == ']')
            return false;

        stack<char> buff;
        map<char, char> m = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for(int i = 0; i < s.length(); i++)
        {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[')
            {
                buff.push(s[i]);
            }
            else
            {
                if(!buff.empty() && buff.top() == m[s[i]])
                    buff.pop();
                else
                    return false;
            }
        }
        return buff.empty();
    }
};
