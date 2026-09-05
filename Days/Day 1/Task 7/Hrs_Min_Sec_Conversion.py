#Take a number of seconds and convert it into: hours + minutes + seconds

seconds=float(input("Enter Seconds: "))

minutes=seconds/60

hours=minutes/60

print(f"seconds: {seconds}\nMinutes: {minutes}\nHours: {hours:.2f}")