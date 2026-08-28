def solution(id_list, report, k):
    report = list(set(report))
    
    reported_counts = {user: 0 for user in id_list}
    
    user_reports = {user: [] for user in id_list}
    
    for r in report:
        reporter, reported = r.split()
        user_reports[reporter].append(reported)
        reported_counts[reported] += 1
        
    banned_users = set()
    for user, count in reported_counts.items():
        if count >= k:
            banned_users.add(user)
            
    answer = []
    for user in id_list:
        mail_count = 0
        for reported in user_reports[user]:
            if reported in banned_users:
                mail_count += 1
        answer.append(mail_count)
        
    return answer