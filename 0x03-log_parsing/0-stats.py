#!/usr/bin/python3
"""
Module with function for processing input lines and calculating statistics
"""
import re
import sys
from collections import defaultdict


def process_input_lines():
    """
    Processes a log line and update metrics
    Raises: KeyboardInterrupt on interruption
    """
    total_file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    lines_processed = 0

    pattern = (
        r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET \/projects\/260 HTTP\/1\.1" '
        r'(\d{3}) (\d+)'
    )
    match = re.match(pattern, line)

    try:
        for line in sys.stdin:
            if match:
                ip, status_code, file_size = match.groups()
                status_code = int(status_code)
                file_size = int(file_size)

                total_file_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print(f'Total file size: {total_file_size}')
                    for code in sorted(status_codes.keys()):
                        if status_codes[code] > 0:
                            print(f'{code}: {status_codes[code]}')       

        if match and (lines_processed < 10 or lines_processed % 10 > 0):
            print(f'Total file size: {total_file_size}')
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f'{code}: {status_codes[code]}')

    except KeyboardInterrupt:
        print(f'Total file size: {total_file_size}')
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f'{code}: {status_codes[code]}')


if __name__ == "__main__":
    process_input_lines()
