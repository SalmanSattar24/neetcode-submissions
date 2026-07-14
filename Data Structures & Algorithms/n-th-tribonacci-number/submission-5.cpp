using namespace std;

class Solution {
public:
    int tribonacci(int n) {
        
        int fib1 = 0;
        int fib2 = 1;
        int fib3 = 1;
        int fib_current = 0;

        if (n == 0) { return 0; }
        if ( n == 1 || n == 2) { return 1; } 

        for (int step = 3; step <= n; step++) {
            
            fib_current = fib1 + fib2 + fib3;

            fib1 = fib2;
            fib2 = fib3;
            fib3 = fib_current;

        }

        return fib_current;

    }
};