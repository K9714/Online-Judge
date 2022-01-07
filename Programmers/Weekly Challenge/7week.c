#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int array_indexof(int* arr, int arr_len, int value) {
    for(int i = 0; i < arr_len; i++) {
        if (arr[i] == value) return i;
    }
    return -1;
}

int* array_delete(int* arr, int* arr_len, int value) {
    if (array_indexof(arr, *arr_len, value) == -1) return arr;
    int idx = 0;
    int* new_arr = (int*)malloc(sizeof(int) * (*arr_len - 1));
    for(int i = 0; i < *arr_len; i++) {
        if (arr[i] == value)
            continue;
        new_arr[idx++] = arr[i];
    }
    *arr_len -= 1;
    free(arr);
    return new_arr;
}

int* solution(int _enter[], int enter_len, int leave[], int leave_len) {
    int idx, l, n = 0;
    int* cnt = (int*)malloc(sizeof(int) * enter_len);
    int* enter = (int*)malloc(sizeof(int) * enter_len);
    for(int i = 0; i < enter_len; i++) {
        cnt[i] = 0;
        enter[i] = _enter[i];
    }
    
    for(int i = 0; i < leave_len; i++) {
        l = leave[i];
        idx = array_indexof(enter, enter_len, l);
        n = n < idx ? idx : n;
        if (n != 0) {
            cnt[l - 1] += n;
            for(int j = 0; j <= n; j++) {
                if (enter[j] == l) continue;
                cnt[enter[j] - 1] += 1;
            }
        }
        n--;
        enter = array_delete(enter, &enter_len, l);
    }
    free(enter);
    return cnt;
}