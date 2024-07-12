// https://leetcode.com/problems/merge-strings-alternately

class Solution {
    public String mergeAlternately(String word1, String word2) {
        boolean isFirstLonger = word1.length() > word2.length();
        int loopLen = isFirstLonger ? word1.length() : word2.length();

        String result = ""; 
        for (int i = 0; i < loopLen; i++) {
            if (i < word1.length()) {
                result += word1.charAt(i);
            }
            if (i < word2.length()) {
                result += word2.charAt(i);
            }
        }

        return result;
    }
}
