import csv
from collections import defaultdict

def vendor_aggregation(filepath="data/raw/invoices.csv"):
    vendors = defaultdict(lambda: {
        "total_invoices": 0,
        "total_amount_inr": 0.0,
        "duplicate_count": 0,
        "pending_count": 0,
        "approved_count": 0
    })

    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            v = row["vendor_name"]
            vendors[v]["total_invoices"] += 1
            vendors[v]["total_amount_inr"] += float(row["amount_inr"])
            if row["flagged"] == "True":
                vendors[v]["duplicate_count"] += 1
            if row["status"] == "Pending":
                vendors[v]["pending_count"] += 1
            if row["status"] == "Approved":
                vendors[v]["approved_count"] += 1

    print(f"\n{'Vendor':<30} {'Invoices':>8} {'Total INR':>12} {'Duplicates':>10} {'Dup%':>6}")
    print("-" * 70)

    import os
    os.makedirs("data/processed", exist_ok=True)

    with open("data/processed/vendor_summary.csv", "w", newline="") as out:
        fieldnames = ["vendor_name", "total_invoices", "total_amount_inr",
                     "duplicate_count", "duplicate_rate_%",
                     "pending_count", "approved_count"]
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        writer.writeheader()

        for vendor, stats in sorted(
            vendors.items(),
            key=lambda x: x[1]["total_amount_inr"],
            reverse=True
        ):
            dup_rate = round(
                stats["duplicate_count"] / stats["total_invoices"] * 100, 2
            )
            print(f"{vendor:<30} {stats['total_invoices']:>8} "
                  f"{stats['total_amount_inr']:>12.2f} "
                  f"{stats['duplicate_count']:>10} {dup_rate:>5}%")
            writer.writerow({
                "vendor_name": vendor,
                **stats,
                "duplicate_rate_%": dup_rate
            })

    print("\nSaved to data/processed/vendor_summary.csv")

if __name__ == "__main__":
    vendor_aggregation()