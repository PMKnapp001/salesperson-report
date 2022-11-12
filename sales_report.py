"""Generate sales report showing total melons each salesperson sold."""


sales_report = {}

file = open('sales-report.txt')

for line in file:
    line = line.rstrip()
    entries = line.split('|')
    if entries[0] in sales_report:
        sales_report[entries[0]] = sales_report[entries[0]] + int(entries[2])
    else:
        sales_report[entries[0]] = int(entries[2])

for salesperson in sales_report.items():
    print(f'{salesperson[0]} sold {salesperson[1]} melons.')