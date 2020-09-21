from datetime import datetime
import sys


def solution():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    dt = datetime(2016,a,b)
    dt = dt.strftime('%a')
    if dt == 'Sun':
        dt = 'SUN'
    elif dt == 'Mon':
        dt = 'MON'
    elif dt == 'Tue':
        dt = 'TUE'
    elif dt == 'Wed':
        dt = 'WED'
    elif dt == 'Thu':
        dt = 'THU'
    elif dt == 'Fri':
        dt = 'FRI'
    elif dt == 'Sat':
        dt = 'SAT'
    return dt

print(solution())