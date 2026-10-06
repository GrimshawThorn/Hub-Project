import sys
from pathlib import Path
import subprocess

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from PySide6.QtCore import Qt

uptime_script = Path(__file__).resolve().parent / "Uptime report.py"

app = QApplication(sys.argv)

app.setStyleSheet("""
    QWidget {
        background-color: #1e1e1e;
        color: #ffffff;
    }

    QWidget#navPanel {
    background-color: #252525;
    border: 1px solid #000000;
}

QWidget#dataPanel {
    background-color: #1e1e1e;
    border: 1px solid #000000;
}
""")

window = QWidget()
window.setWindowTitle("Learning App")
window.resize(900, 900)

label_two = QLabel("Navigation")
label_three = QLabel("Data Area")

uptime_result = subprocess.run(
    [
        sys.executable,
        str(uptime_script)
    ],
    capture_output=True,
    text=True)

print(uptime_result.stdout)

label_three.setText(uptime_result.stdout.strip())

nav_panel = QWidget()
data_panel = QWidget()

layout = QHBoxLayout()

Nav_layout = QVBoxLayout(nav_panel)
Data_layout = QVBoxLayout(data_panel)

layout.addWidget(nav_panel, 1)
layout.addWidget(data_panel, 3)

Nav_layout.addWidget(label_two)
Data_layout.addWidget(label_three)

nav_panel.setObjectName("navPanel")
data_panel.setObjectName("dataPanel")

window.setLayout(layout)

window.show()

app.exec()