import csv
import os


total_months = 0
total_profit = 0
previous_profit = 0
profit_change_list = []
months_list = []
average_change = 0

with open('./Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        month = row[0]
        profit = int(row[1])

        total_months += 1

        total_profit += profit

        if previous_profit != 0:
            profit_change = profit - previous_profit
            profit_change_list.append(profit_change)
            months_list.append(month)
        previous_profit = profit

average_change = sum(profit_change_list) / len(profit_change_list)

greatest_increase = max(profit_change_list)
greatest_decrease = min(profit_change_list)

increase_month = months_list[profit_change_list.index(greatest_increase)]
decrease_month = months_list[profit_change_list.index(greatest_decrease)]

fv_average_change = "{:.2f}".format(average_change)


print("----------------------------------------------------------------")
print("Financial Analysis")
print("-------------------------------------------------")

print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${fv_average_change}')
print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')
print("----------------------------------------------------------------")
