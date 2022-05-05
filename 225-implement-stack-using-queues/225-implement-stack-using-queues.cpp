class MyStack {
public:
    vector<int> stack;
    MyStack() {
        
    }
    
    void push(int x) {
        stack.push_back(x);
    }
    
    int pop() {
        int v = stack.back();
        stack.pop_back();
        return v;
    }
    
    int top() {
        return stack.back();
    }
    
    bool empty() {
        return stack.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */