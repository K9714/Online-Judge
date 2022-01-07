import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] _enter, int[] leave) {
        ArrayList<Integer> enter = (ArrayList<Integer>)Arrays.stream(_enter).boxed().collect(Collectors.toList());
        int[] cnt = new int[_enter.length];
        int n = 0;
        for(int l : leave) {
            int idx = enter.indexOf(l);
            n = n < idx ? idx : n;
            cnt[l - 1] += n;
            enter.remove(Integer.valueOf(l));
            for(int i = 0; i < n; i++)
                cnt[enter.get(i) - 1] += 1;
            n--;
        }
        return cnt;
    }
}