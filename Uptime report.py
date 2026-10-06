#System uptime project.

import subprocess
from datetime import datetime
#command line request for os start time.
os_start = subprocess.run(
   [
    "powershell",
    "-Command",
    "(Get-CimInstance Win32_OperatingSystem).LastBootUpTime"
   ],
   capture_output=True,
   text=True
)

#Date time setup
boot_time = datetime.strptime(
    os_start.stdout.strip(),
    "%A, %B %d, %Y %I:%M:%S %p"
)

current_time = datetime.now()

uptime = current_time - boot_time

print(uptime)