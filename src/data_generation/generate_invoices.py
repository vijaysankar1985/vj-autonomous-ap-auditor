import csv
import random
import os
from faker import Faker
from datetime import date, timedelta

fake = Faker()

VENDORS = [
    "Tata Consultancy Services", "Infosys Ltd", "Wipro Technologies",
    "HCL Technologies", "Tech Mahindra", "Cognizant",
    "Capgemini India", "Accenture Solutions", "IBM India", "Oracle India"
]

CATEGORIES = [
    "IT Services", "Consulting", "Software License",
    "Hardware", "Maintenance", "Cloud Services", "Professional Services"
]

def random_date(start_days_ago, end_days_from_now):
    start = date.today() - timedelta(days=start_days_ago)
    end = date.today() + timedelta(days=end_days_from_now)
    delta = (end - start).days
    return (start + timedelta(days=random.randint(0, delta))).strftime("%Y-%m-%d")

def generate_invoices(n=100):
    os.makedirs("data/raw", exist_ok=True)
    invoices = []
    for i in range(n):
        is_duplicate = random.random() < 0.10
        invoices.append({
            "invoice_id": f"INV-{1000 + i}",
            "vendor_name": random.choice(VENDORS),
            "invoice_date": random_date(180, 0),
            "due_date": random_date(0, 60),
            "amount_inr": round(random.uniform(5000, 500000), 2),
            "category": random.choice(CATEGORIES),
            "status": "Duplicate" if is_duplicate else random.choice(
                ["Approved", "Pending", "Rejected"]
            ),
            "po_number": f"PO-{random.randint(5000, 9999)}",
            "flagged": is_duplicate
        })

    with open("data/raw/invoices.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=invoices[0].keys())
        writer.writeheader()
        writer.writerows(invoices)

    duplicates = sum(1 for inv in invoices if inv["flagged"])
    print(f"Generated {len(invoices)} invoices")
    print(f"Duplicates injected: {duplicates}")
    for inv in invoices[:3]:
        print(inv)

if __name__ == "__main__":
    generate_invoices(100)