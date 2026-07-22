all_time = '1h 45m,360s,25m,30m 120s,2h 60s'
summary_minutes = 0
summary_seconds = 0

for time in all_time.split(','): 
    for part in time.split(' '):
        if 'h' in part:
            summary_minutes += int(part.replace('h','')) * 60
        elif 's' in part:
            summary_seconds += int(part.replace('s',''))
        elif 'm' in part: 
            summary_minutes += int(part.replace('m',''))

print(int(summary_minutes + summary_seconds/60))