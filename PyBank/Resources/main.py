
def read_csv(file_path):
    dates = []
    profits_losses = []
    with open(file_path, 'r') as file:
        next(file)  
        for line in file:
            date, profit_loss = line.strip().split(',')
            dates.append(date)
            profits_losses.append(int(profit_loss))
    return dates, profits_losses


def calculate_total_months_and_net_total(profits_losses):
    total_months = len(profits_losses)
    net_total = sum(profits_losses)
    return total_months, net_total


def calculate_changes_and_extremes(dates, profits_losses):
    changes = [profits_losses[i] - profits_losses[i-1] for i in range(1, len(profits_losses))]

    average_change = sum(changes) / len(changes)

    max_increase_amount = max(changes)
    max_increase_index = changes.index(max_increase_amount) + 1  
    max_increase_date = dates[max_increase_index]

    max_decrease_amount = min(changes)
    max_decrease_index = changes.index(max_decrease_amount) + 1  
    max_decrease_date = dates[max_decrease_index]

    return changes, average_change, max_increase_date, max_increase_amount, max_decrease_date, max_decrease_amount

def write_results_to_text_file(output_file, total_months, net_total, average_change, max_increase_date, max_increase_amount, max_decrease_date, max_decrease_amount):
    with open(output_file, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Net Total: ${net_total}\n")
        file.write(f"Average Change: ${average_change:.2f}\n")
        file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount:.2f})\n")
        file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount:.2f})\n")

file_path = 'PyBank/Resources/budget_data.csv'
output_folder = 'PyBank/Analysis'
output_file = output_folder + 'financial_analysis.txt'
dates, profits_losses = read_csv(file_path)

total_months, net_total = calculate_total_months_and_net_total(profits_losses)

changes, average_change, max_increase_date, max_increase_amount, max_decrease_date, max_decrease_amount = calculate_changes_and_extremes(dates, profits_losses)


print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount:.2f})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount:.2f})")

write_results_to_text_file(output_file, total_months, net_total, average_change, max_increase_date, max_increase_amount, max_decrease_date, max_decrease_amount)

print(f"Results exported to '{output_file}'.")