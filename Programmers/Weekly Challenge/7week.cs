using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] _enter, int[] leave) {
        int n = 0;
        int[] answer;
        List<int> cnt = new List<int>();
        List<int> enter = new List<int>();
        foreach(int e in _enter) {
            cnt.Add(0);
            enter.Add(e);
        }
        
        foreach(int l in leave) {
            int idx = enter.IndexOf(l);
            n = n < idx ? idx : n;
            if (n != 0) {
                cnt[l - 1] += n;
                for(int i = 0; i <= n; i++) {
                    if (enter[i] == l) continue;
                    cnt[enter[i] - 1] += 1;
                }
            }
            n -= 1;
            enter.Remove(l);
        }
        return cnt.ToArray();
    }
}