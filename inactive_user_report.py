import csv
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("run.log", encoding="utf-8")
    ]
)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate inactive user report from CSV"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input CSV file (e.g. users.csv)"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output CSV file"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=90,
        help="Inactivity threshold in days (default: 90)"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        inactive_users = []

        with open(args.input, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["last_login_days"]) > args.days:
                    inactive_users.append(row)

        with open(args.output, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["username", "last_login_days", "department"]
            )
            writer.writeheader()
            writer.writerows(inactive_users)

        logging.info(
            "Completed. %d inactive users written to %s (threshold=%d days)",
            len(inactive_users),
            args.output,
            args.days
        )

    except FileNotFoundError as e:
        logging.error("File not found: %s", e)

    except ValueError as e:
        logging.error("Invalid data format: %s", e)

    except Exception:
        logging.exception("Unexpected error occurred")


if __name__ == "__main__":
    main()
