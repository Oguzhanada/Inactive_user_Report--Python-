\# Inactive User Report (Python CLI)



Python script that reads user activity data from a CSV file and generates an "inactive users" report based on a configurable inactivity threshold.



\## Features

\- CSV parsing with `csv.DictReader`

\- CLI parameters via `argparse`

\- Structured logging + error handling

\- Outputs a filtered CSV report



\## Usage

```bash

python inactive\_user\_report.py --input sample\_users.csv --output inactive\_users.csv --days 90



