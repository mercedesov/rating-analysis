
import argparse
import csv
from tabulate import tabulate
from reports.average_rating import average_rating_report

def read_files(files):
    rows = []
    for file in files:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows.extend(reader)
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)
    args = parser.parse_args()

    data = read_files(args.files)

    reports = {
        'average-rating': average_rating_report
    }

    if args.report not in reports:
        print('Unknown report')
        return

    report_func = reports[args.report]
    table = report_func(data)
    print(tabulate(table, headers=["Brand", "Average Rating"], tablefmt="grid"))

if __name__ == "__main__":
    main()
