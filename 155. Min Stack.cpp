class MinStack {
public:
    stack<int> s;
    stack<int> min_s;

    void push(int val) {
        s.push(val);
        if(!min_s.empty()) min_s.push(min(min_s.top(), val));
        else min_s.push(val);
    }

    void pop() {
        if(!s.empty())
        {
            s.pop();
            min_s.pop();
        }
    }

    int top() {
        if(!s.empty()) return s.top();
        else return NULL;
    }

    int getMin() {
        if(!min_s.empty()) return min_s.top();
        else return NULL;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
