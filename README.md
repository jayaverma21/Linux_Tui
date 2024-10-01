# Linux_Tui_Program

This is a simple Terminal User Interface (TUI) program written in Python that allows users to run basic Linux commands either on a local system or a remote system via SSH. It requires user authentication before executing any commands.

## Features

- **Local Commands:**
  - Display the current date.
  - Display a calendar.
  - List directory contents.
  - Create a new user on the local machine.
  
- **Remote Commands (via SSH):**
  - Display the current date on a remote system.
  - Display a calendar on a remote system.
  - List directory contents of a remote system.
  - Create a new user on the remote system.

## Prerequisites

Before running the program, ensure you have the following:

- Python 3.x installed.
- SSH service enabled if running commands on a remote machine.
- Remote system credentials (IP and password).
- Proper SSH configuration for connecting to remote systems.
  
## Usage

1. Clone this repository or copy the script into a Python file.
2. Run the program in the terminal using the command:

   ```bash
   python3 <your_script_name>.py
