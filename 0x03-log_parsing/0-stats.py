#!/usr/bin/python3
"""
Log parsing
"""
import re
import sys
from collections import defaultdict


def process_log_line(line, total_file_size, status_code_count):
    """Processes a log line and update metrics"""
    log_format = re.compile(
        r'(\d+\.\d+\.\d+\.\d+) - \[.*\] '
        r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)'
        )
    match = log_format.match(line)

    if match:
        ip, status_code, file_size = match.groups()

        # Update total file size
        total_file_size += int(file_size)

        # Update status code count
        if status_code in {'200', '301', '400',
                           '401', '403', '404', '405', '500'}:
            status_code_count[status_code] += 1

    return total_file_size, status_code_count


def print_statistics(total_file_size, status_code_count):
    """Print the computed statistics"""
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_count.keys()):
        print(f'{code}: {status_code_count[code]}')


def main():
    """Read log lines and prints statistics"""
    total_file_size = 0
    status_code_count = defaultdict(int)
    line_number = 0

    try:
        for line in sys.stdin:
            line_number += 1

            total_file_size, status_code_count = process_log_line(
                line, total_file_size, status_code_count)

            # Print statistics after every 10 lines
            if line_number % 10 == 0:
                print_statistics(total_file_size, status_code_count)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_statistics(total_file_size, status_code_count)


if __name__ == "__main__":
    main()
