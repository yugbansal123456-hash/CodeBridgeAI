#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<string> words = {"the", "cat", "and", "the", "dog", "and", "the", "bird"};
    map<string, int> counts;
    for (const string& w : words) {
        counts[w]++;
    }
    for (const auto& kv : counts) {
        cout << kv.first << ": " << kv.second << endl;
    }
    cout << "Unique words: " << counts.size() << endl;

    vector<int> nums;
    for (int i = 1; i <= 5; i++) nums.push_back(i * i);
    nums.pop_back();
    nums.insert(nums.begin(), 0);
    cout << "Vector:";
    for (int x : nums) cout << " " << x;
    cout << endl;
    cout << "Size: " << nums.size() << ", front: " << nums.front() << ", back: " << nums.back() << endl;
    return 0;
}
