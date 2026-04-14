class Solution {
    Set<Integer> set=new HashSet<>();
    public boolean hasDuplicate(int[] nums) {
        for(int num:nums){
            if (!set.contains(num)){
                set.add(num);
            }else{
                return true;
            }
        }
        return false;
        
    }
}