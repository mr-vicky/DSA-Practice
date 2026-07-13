class Solution {
public:
    bool isAnagram(string s, string t) {
        int l1 = s.length();
        int l2 = t.length();

        if(l1 != l2) return false; // if lengths are not the same
        
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        for(int i = 0; i < l1; i++){
            if(s[i] != t[i]){
                cout << s[i] << " " << t[i] << endl;
                return false;
            }
        }
        return true;
    }
};
