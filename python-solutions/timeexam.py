n = int(input())

# calculate the number of hours and minutes
hours = n // 60
minutes = n % 60

# calculate the resulting hour and minute in 24-hour clock format
result_hour = (hours % 24)
result_minute = minutes

# format the output string with leading zeros if necessary
output = f"{result_hour:02d}{result_minute:02d}"

print(output)
