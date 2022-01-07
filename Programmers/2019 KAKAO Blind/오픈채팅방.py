import re
def solution(record):
    msg = []
    udata = {}
    p = re.compile("(Enter|Leave|Change) (.*)")
    for r in record:
        m = p.match(r)
        kind = m.group(1)
        if kind == "Leave":
            user = m.group(2)
            msg.append([user, f"{user}님이 나갔습니다."])
        else:
            user, name = m.group(2).split()
            udata[user] = name
            if kind == "Enter":
                msg.append([user, f"{user}님이 들어왔습니다."])
    
    for i in range(len(msg)):
        msg[i] = msg[i][1].replace(msg[i][0], udata[msg[i][0]])
        
    return msg