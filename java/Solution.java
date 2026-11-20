import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        ArrayList<int[]> arr=new ArrayList<>();
        HashMap<Integer,Integer> d=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            d.put(nums[i], d.getOrDefault(nums[i], 0) + 1);
        }
        for(int key : d.keySet()){
            arr.add(new int[]{-d.get(key), key});
        }
        PriorityQueue<int[]> h = new PriorityQueue<>(
    (a, b) -> Integer.compare(a[0], b[0])
);
        h.addAll(arr);
        int[] res=new int[k];
        for(int i=0;i<k;i++){
            int[] tem=h.poll();
            res[i]=tem[1];
        }
        return res;
    }
}