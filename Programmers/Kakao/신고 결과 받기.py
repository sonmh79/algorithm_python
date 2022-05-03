from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report_d = defaultdict(list)
    report_cnt_d = defaultdict(int)
    for r in report:
        user,reported_user = r.split()
        if reported_user not in report_d[user]:
            report_d[user].append(reported_user)
            report_cnt_d[reported_user] += 1
    
    black_list = []
    for user in report_cnt_d:
        if report_cnt_d[user] >= k:
            black_list.append(user)
    
    for user in id_list:
        cnt = 0
        for bad_user in report_d[user]:
            if bad_user in black_list:
                cnt += 1
        answer.append(cnt)
        
    return answer