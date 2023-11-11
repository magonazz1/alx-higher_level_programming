#!/usr/bin/python3
"""
101-stats.py - Script to compute and print metrics based on input data.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints the following statistics:
1. Total file size: File size: <total size>
2. Number of lines by status code:
   - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
   - Format: <status code>: <number> (status codes printed in ascending order)
"""

import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    """
    Print file size and status code statistics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts for each status code.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    """
    Main function to read input, compute metrics, and print statistics.
    """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

