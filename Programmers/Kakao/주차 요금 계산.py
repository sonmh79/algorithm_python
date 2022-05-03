from collections import defaultdict
def solution(fees, records):
    answer = []
    d = defaultdict(list)
    for record in records:
        time, car, status = record.split(" ")
        if status == "IN":
            d[car].append([time, "23:59"])
        else:
            d[car][-1][1] = time
            
    for car in sorted(d):
        fee = 0
        t = 0
        for log in d[car]:
            in_time, out_time = log
            in_h, in_m = in_time.split(":")
            out_h, out_m = out_time.split(":")

            in_h, in_m, out_h, out_m = int(in_h), int(in_m), int(out_h), int(out_m)

            if out_m - in_m < 0:
                out_h -= 1
                out_m += 60     
            t += out_m - in_m
            t += (out_h - in_h) * 60

        if t <= fees[0]:
            fee += fees[1]
        else:
            res = fees[1]
            n,r = divmod(t-fees[0],fees[2])
            res += fees[3] * n
            if r != 0:
                res += fees[3]
            fee += res
        answer.append(fee)
        
    return answer