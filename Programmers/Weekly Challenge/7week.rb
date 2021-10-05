def solution(enter, leave)
    cnt = Array.new(enter.size, 0)
    n = 0
    leave.each do |l|
        idx = enter.index(l)
        n = n < idx ? idx : n
        if n != 0
            cnt[l - 1] += n
            (n + 1).times do |i|
                next if enter[i] == l
                cnt[enter[i] - 1] += 1
            end
        end
        n -= 1
        enter.delete(l)
    end
    return cnt
end