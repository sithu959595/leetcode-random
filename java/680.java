class Solution {
    public boolean validPalindrome(String s) {
        boolean[] chance=new boolean[1]; 
        return recur(chance, s,0,s.length()-1);
    }
    private boolean recur(boolean[] chance,String s,int l,int r){
        if(l>=r){
            return true;
        }
        if(s.charAt(l)==s.charAt(r)){
            return recur(chance,s,l+1,r-1);
        }
        else{
            if(chance[0]){
                chance[0]=false;
                return recur(chance,s,l+1,r) || recur(chance,s,l,r-1);
            }
            else{
                return false;
            }
        }
    }
}