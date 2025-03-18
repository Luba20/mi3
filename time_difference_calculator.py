from datetime import datetime
import sys

def parse_timestamp(timestamp):
    return datetime.strptime(timestamp, "%a %d %b %Y %H:%M:%S %z")

def time_difference(t1, t2):
    dt1 = parse_timestamp(t1)
    dt2 = parse_timestamp(t2)
    return abs(int((dt1 - dt2).total_seconds()))

def main():
    T = int(sys.stdin.readline().strip())
    results = []
    for _ in range(T):
        t1 = sys.stdin.readline().strip()
        t2 = sys.stdin.readline().strip()
        results.append(time_difference(t1, t2))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
