// TC: O(M*N)
// SC: O(M)
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group;

        for(const auto& s: strs){
            vector<int>count(26, 0);

            for(auto c: s){
                count[c - 'a']++;
            }

            string key = to_string(count[0]);
            for(int i = 1; i < count.size(); i++){
                key += ',' + to_string(count[i]);
            }
            group[key].push_back(s);
        }

        vector<vector<string>> result;
        for(const auto& g: group){
            result.push_back(g.second);
        }
        return result;
    }
};
