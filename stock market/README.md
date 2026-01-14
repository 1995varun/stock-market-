# Indian Stock Market Automation

This tool automates the process of finding the top Indian stocks by aggregating data from:
- **Google News**: Recent articles and market analysis.
- **YouTube**: Trending videos from financial influencers and analysts.

## Prerequisites

- Python 3.x installed.

## Installation

1. Open your terminal or command prompt.
2. Navigate to this directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```bash
python main.py
```

Follow the on-screen prompts to input your search queries (e.g., "Penny stocks India", "Blue chip stocks 2026") or press Enter to use the optimized defaults.

## Output

- The tool displays a summary in the terminal.
- It also saves a text file `stock_report.txt` with the links for later reference.

## Troubleshooting

If you see errors like `'python' is not recognized` or `'pip' is not recognized`:

1.  **Install Python**: Ensure Python is installed from [python.org](https://www.python.org/downloads/).
2.  **Add to PATH**: During installation, check the box **"Add Python to PATH"**.
3.  **Try Python Launcher**: Try using `python3` or `py` instead of `python`:
    ```bash
    python3 -m pip install -r requirements.txt
    python3 main.py
    ```

## Automation Features

### 1. Infographic Generation
The tool automatically generates a visual summary `stock_infographic.png` using a "Nano Banan" inspired aesthetic (Neon Green on Dark Blue).

### 2. Weekly Email Automation
The tool is configured to email reports to `varunlakebright04@gmail.com`.

**Setup:**
1.  **Get an App Password** for the sender account (`varunlakebright04@gmail.com`):
    - Go to Google Account > Security > 2-Step Verification > App passwords.
    - Create one for "Mail" / "Windows Computer".
2.  **Set Environment Variables**:
    - **PowerShell**:
      ```powershell
      $env:GMAIL_USER = "varunlakebright04@gmail.com"
      $env:GMAIL_PASS = "nlor yqzy rtxe jjow"
      ```
    - **CMD**:
      ```cmd
      set GMAIL_USER=varunlakebright04@gmail.com
      set GMAIL_PASS=nlor yqzy rtxe jjow
      ```

### 3. Scheduling (Windows Task Scheduler)
To run this weekly:
1.  Open **Task Scheduler**.
2.  Create a Basic Task -> "Weekly Stock Report".
3.  Trigger: Weekly (select your day).
4.  Action: Start a program.
    - Program: `python` (or full path to python.exe)
    - Arguments: `main.py --auto`
    - Start in: `c:\Users\OM\Documents\stock market`

