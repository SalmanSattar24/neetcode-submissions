using namespace std;

class Solution {
public:
    int tribonacci(int n) {
        
        unordered_map<int, int> tab = {{0, 0,}, {1, 1}, {2, 1}};

        for (int step = 3; step <= n; step++) {

            int fib1 = tab.count(step - 1) ? tab[step - 1] : 0;
            int fib2 = tab.count(step - 2) ? tab[step - 2] : 0;
            int fib3 = tab.count(step - 3) ? tab[step - 3] : 0;

            int fib = fib1 + fib2 + fib3;

            tab[step] = fib;
        }

        return tab[n];

    }
};