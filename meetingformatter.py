from datetime import datetime

meeting = datetime(2026, 7, 6, 9, 0) 

print(meeting.strftime("%d/%m/%Y"))
print(meeting.strftime("%B %d, %Y at %I:%M %p"))
print(meeting.strftime("%A %d %B %Y"))
