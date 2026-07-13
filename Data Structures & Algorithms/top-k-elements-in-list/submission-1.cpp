// TC: O(N*N)
// SC: O(N)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> ump;
        for(auto x: nums){
            ump[x]++;
        }

        vector<int> count;
        for(auto x: ump){
            count.push_back(x.second);
        }
        sort(count.begin(), count.end(), greater<int>());

        vector<int>res; 
        int i = 0;
        while(i < k){
            for(auto& x: ump){
                if(x.second == count[i]){
                    res.push_back(x.first);
                    x.second = -1;
                }
            }
            i++;
        }
        return res;
    }
};
