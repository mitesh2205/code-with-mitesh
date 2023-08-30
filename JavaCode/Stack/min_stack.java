import java.util.Stack;

public class min_stack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    
    public min_stack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        if (!stack.isEmpty()) {
            if (stack.peek().equals(minStack.peek())) {
                minStack.pop();
            }
            stack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }

    public static void main(String[] args) {
        min_stack obj = new min_stack();
        obj.push(5);
        obj.push(3);
        obj.push(2);
        obj.push(1);
        obj.pop();
        int param_3 = obj.top();
        int param_4 = obj.getMin();
        System.out.println(param_3); // Output: 2
        System.out.println(param_4); // Output: 2
    }
}
