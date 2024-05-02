//
// Created by abuub on 02/05/2024.
//
#include <algorithm>
#include<iostream>
#include <vector>
#include<unordered_map>
using namespace std;
int findMax(vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    int n = nums.size();
    for (int i = n-1; i >= 0; i--) {
        if (nums[i] > 0 && std::binary_search(nums.begin(), nums.end(), -nums[i])) {
            return nums[i];
        }
    }
    return -1;  // If no such pair found
}

int main() {
    vector<int>nums1;
    vector<int>nums2;
    vector<int>nums3;

    nums1 = {-1,2,-3,3};
    cout<<findMax(nums1);
    cout<<endl;

    nums2 = {-1,10,6,7,-7,1};
    cout<<findMax(nums2);
    cout<<endl;

    nums3 = {-10,8,6,7,-2,-3};
    cout<<findMax(nums3);
    cout<<endl;
    return 0;
}