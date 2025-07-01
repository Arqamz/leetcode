class Solution {
public:
    int possibleStringCount(string word) {
        int counter = 1;
        int i = 0;
        while (i < word.length()) {
            char curr = word[i];
            while (i < word.length() && word[++i] == curr) {
                counter++;
            }
        }
        return counter;
    }
};
