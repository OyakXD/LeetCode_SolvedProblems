class Solution {
    public int arraySign(int[] nums) {
        int n = nums.length;
        double pro = 1;
        for (int i =0; i < n; i++){
            pro *= nums[i];
        }

        if (pro>0){
            return 1;
        } else if (pro < 0){
            return -1;
        } 
        return 0;
    }
}