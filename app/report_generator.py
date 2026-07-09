"""
============================================================
SSL Certificate Expiry Monitoring System
Report Generator Module
============================================================

Author  : Pritesh Thamke
Version : 1.0
"""

import csv
import os


# ==========================================================
# CSV REPORT
# ==========================================================

def generate_csv_report(results):
    """
    Generate CSV Report
    """

    # Create reports folder
    os.makedirs("reports", exist_ok=True)

    # CSV file path
    report_file = os.path.join(
        "reports",
        "ssl_report.csv"
    )

    with open(report_file, mode="w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        fieldnames = [
    "Website",
    "Common Name",
    "Issuer",
    "Expiry Date",
    "Remaining Days",
    "Status"
]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
)

        writer.writeheader()

        for result in results:

            writer.writerow({

                "Website": result["website"],

                "Common Name": result["common_name"],

                "Issuer": result["issuer"],

                "Expiry Date": result["expiry_date"],

                "Remaining Days": result["remaining_days"],

                "Status": result["status"]

    })


# ==========================================================
# HTML DASHBOARD
# ==========================================================

def generate_html_report(results):
    """
    Generate HTML Dashboard
    """

    # Create reports folder
    os.makedirs("reports", exist_ok=True)

    # HTML file path
    html_file = os.path.join(
        "reports",
        "ssl_dashboard.html"
    )

    with open(html_file, mode="w", encoding="utf-8") as file:

        # ==========================================
        # HTML START
        # ==========================================

        file.write("""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>SSL Certificate Dashboard</title>

<style>

body{

    font-family: Arial, sans-serif;

    background:#f4f6f9;

    margin:40px;

}

h1{

    text-align:center;

    color:#1f4e79;

}

h3{

    color:#1f4e79;

}

table{

    width:100%;

    border-collapse:collapse;

    background:white;

}

th{

    background:#1f4e79;

    color:white;

    padding:12px;

}

td{

    padding:10px;

    border:1px solid #ddd;

    text-align:center;

}

tr:nth-child(even){

    background:#f8f8f8;

}

</style>

</head>

<body>

<h1>SSL Certificate Monitoring Dashboard</h1>

<hr>

<h3>Website SSL Report</h3>

<table>

<tr>

<th>Website</th>

<th>Common Name</th>

<th>Issuer</th>

<th>Expiry Date</th>

<th>Remaining Days</th>

<th>Status</th>

</tr>

""")

        # ==========================================
        # DYNAMIC TABLE ROWS
        # ==========================================

        for result in results:

            file.write(f"""
<tr>

<td>{result['website']}</td>

<td>{result['common_name']}</td>

<td>{result['issuer']}</td>

<td>{result['expiry_date']}</td>

<td>{result['remaining_days']}</td>

<td>{result['status']}</td>

</tr>
""")

        # ==========================================
        # HTML END
        # ==========================================

        file.write("""
</table>

</body>

</html>
""")