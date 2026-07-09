"""
====================================================================
SSL Certificate Monitoring System
====================================================================

Author  : Pritesh Thamke
Version : 3.0

Description:
Professional SSL Certificate Monitoring System

Features
--------
✔ SSL Certificate Monitoring
✔ Certificate Expiry Detection
✔ CSV Report Generation
✔ HTML Dashboard
✔ Email Notification
✔ Logging
✔ YAML Configuration Support

====================================================================
"""

# ==================================================================
# IMPORT MODULES
# ==================================================================

from datetime import datetime
from logging import config

from logger import setup_logger

from ssl_checker import read_websites

from ssl_certificate import (
    get_ssl_certificate,
    get_common_name,
    get_issuer_name,
    get_expiry_date,
    calculate_remaining_days,
    get_ssl_status
)

from report_generator import (
    generate_csv_report,
    generate_html_report
)

from email_sender import send_email

from config_reader import load_config


# ==================================================================
# LOGGER
# ==================================================================

logger = setup_logger()


# ==================================================================
# MAIN FUNCTION
# ==================================================================

def main():

    # ==============================================================
    # LOAD CONFIGURATION
    # ==============================================================

    config = load_config()

    # ==============================================================
    # PROJECT INFORMATION
    # ==============================================================

    project_name = config["project"]["name"]

    project_version = config["project"]["version"]

    project_author = config["project"]["author"]

    # ==============================================================
    # REPORT CONFIGURATION
    # ==============================================================

    csv_report = config["reports"]["csv"]

    html_report = config["reports"]["html"]

    # ==============================================================
    # EMAIL CONFIGURATION
    # ==============================================================

    to_emails = config["email"]["to"]

    cc_emails = config["email"]["cc"]

    bcc_emails = config["email"]["bcc"]

    # ==============================================================
    # START TIMER
    # ==============================================================

    start_time = datetime.now()

    logger.info("=" * 70)
    logger.info(project_name)
    logger.info(f"Version : {project_version}")
    logger.info(f"Author  : {project_author}")
    logger.info("=" * 70)

    logger.info(f"Monitoring Started : {start_time}")

        # ==============================================================
    # PROJECT HEADER
    # ==============================================================

    print("\n")
    print("=" * 70)
    print(f"{project_name}")
    print("=" * 70)
    print(f"Version : {project_version}")
    print(f"Author  : {project_author}")
    print("=" * 70)

    logger.info("Loading websites list...")

    # ==============================================================
    # READ WEBSITE LIST
    # ==============================================================

    websites = read_websites()

    # ==============================================================
    # VALIDATE WEBSITE LIST
    # ==============================================================

    if not websites:

        logger.error("No websites found inside websites.txt")

        print("\nNo websites found in websites.txt")

        return

    total_websites = len(websites)

    logger.info(f"Total Websites Loaded : {total_websites}")

    print(f"\nTotal Websites Found : {total_websites}")

    print("\nStarting SSL Certificate Monitoring...\n")

    # ==============================================================
    # RESULTS STORAGE
    # ==============================================================

    results = []

    logger.info("Results list initialized successfully.")

    # ==============================================================
    # START WEBSITE LOOP
    # ==============================================================

    for website in websites:

        website = website.strip()

        if website == "":
            continue

        logger.info("-" * 70)
        logger.info(f"Checking Website : {website}")

        print("-" * 70)
        print(f"Checking Website : {website}")

        try:

            logger.debug(f"Connecting to {website}")

            # ======================================================
            # GET SSL CERTIFICATE
            # ======================================================

            certificate = get_ssl_certificate(website)

            logger.debug("SSL Certificate Retrieved Successfully")

                        # ======================================================
            # EXTRACT CERTIFICATE INFORMATION
            # ======================================================

            common_name = get_common_name(certificate)

            issuer = get_issuer_name(certificate)

            expiry_date = get_expiry_date(certificate)

            remaining_days = calculate_remaining_days(expiry_date)

            status = get_ssl_status(remaining_days)

            logger.debug("Certificate information extracted successfully.")

            # ======================================================
            # SAVE RESULT
            # ======================================================

            results.append({

                "website": website,

                "common_name": common_name,

                "issuer": issuer,

                "expiry_date": expiry_date,

                "remaining_days": remaining_days,

                "status": status

            })

            logger.debug("Website information added into results list.")

            # ======================================================
            # PROFESSIONAL LOGGING
            # ======================================================

            logger.info(
                f"Website={website} | "
                f"CommonName={common_name} | "
                f"Issuer={issuer} | "
                f"ExpiryDate={expiry_date} | "
                f"RemainingDays={remaining_days} | "
                f"Status={status}"
            )

            # ======================================================
            # CONSOLE OUTPUT
            # ======================================================

            print(f"Website          : {website}")

            print(f"Common Name      : {common_name}")

            print(f"Issuer           : {issuer}")

            print(f"Expiry Date      : {expiry_date}")

            print(f"Remaining Days   : {remaining_days}")

            print(f"Status           : {status}")

            print("-" * 70)

                    # ======================================================
        # EXCEPTION HANDLING
        # ======================================================

        except Exception as error:

            logger.error("=" * 70)
            logger.error(f"Website : {website}")
            logger.error(f"Reason  : {error}")
            logger.error("=" * 70)

            print(f"Website          : {website}")
            print("Common Name      : N/A")
            print("Issuer           : N/A")
            print("Expiry Date      : N/A")
            print("Remaining Days   : N/A")
            print("Status           : ❌ ERROR")
            print(f"Reason           : {error}")
            print("-" * 70)

            results.append({

                "website": website,

                "common_name": "N/A",

                "issuer": "N/A",

                "expiry_date": "N/A",

                "remaining_days": "N/A",

                "status": "❌ ERROR"

            })

            logger.warning(
                f"{website} added to results with ERROR status."
            )

    # ==========================================================
    # WEBSITE SCAN COMPLETED
    # ==========================================================

    logger.info("=" * 70)
    logger.info("Website scanning completed.")
    logger.info(f"Total Websites Processed : {len(results)}")
    logger.info("=" * 70)

    print("\n")
    print("=" * 70)
    print("SSL CERTIFICATE SCANNING COMPLETED")
    print("=" * 70)

    print(f"Total Websites Processed : {len(results)}")

    print("=" * 70)

    # ==========================================================
    # GENERATE REPORTS
    # ==========================================================

    logger.info("Generating CSV Report...")

    generate_csv_report(results)

    logger.info("CSV Report Generated Successfully")

    logger.info("Generating HTML Dashboard...")

    generate_html_report(results)

    logger.info("HTML Dashboard Generated Successfully")

        # ==========================================================
    # SUMMARY STATISTICS
    # ==========================================================

    total_websites = len(results)

    safe_count = 0

    warning_count = 0

    critical_count = 0

    error_count = 0

    # ==========================================================
    # COUNT CERTIFICATE STATUS
    # ==========================================================

    for result in results:

        status = str(result["status"])

        if "SAFE" in status:

            safe_count += 1

        elif "WARNING" in status:

            warning_count += 1

        elif "CRITICAL" in status:

            critical_count += 1

        elif "ERROR" in status:

            error_count += 1

    # ==========================================================
    # PRINT SUMMARY
    # ==========================================================

    print("\n")
    print("=" * 70)
    print("SSL CERTIFICATE SUMMARY")
    print("=" * 70)

    print(f"Total Websites       : {total_websites}")

    print(f"SAFE Certificates    : {safe_count}")

    print(f"WARNING Certificates : {warning_count}")

    print(f"CRITICAL Certificates: {critical_count}")

    print(f"ERROR Websites       : {error_count}")

    print("=" * 70)

    # ==========================================================
    # LOGGER SUMMARY
    # ==========================================================

    logger.info("=" * 70)

    logger.info("SSL Certificate Summary")

    logger.info("=" * 70)

    logger.info(f"Total Websites       : {total_websites}")

    logger.info(f"SAFE Certificates    : {safe_count}")

    logger.info(f"WARNING Certificates : {warning_count}")

    logger.info(f"CRITICAL Certificates: {critical_count}")

    logger.info(f"ERROR Websites       : {error_count}")

    logger.info("=" * 70)

    # ==========================================================
    # PREPARE EMAIL
    # ==========================================================

    today = datetime.now().strftime("%d-%m-%Y")

    subject = f"{project_name} | {today}"

        # ==========================================================
    # HTML EMAIL BODY
    # ==========================================================

    body = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<style>

body {{
    font-family: Arial, Helvetica, sans-serif;
    background-color: #f4f4f4;
}}

.container {{
    width: 700px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 10px;
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th {{
    background:#1565C0;
    color:white;
    padding:12px;
}}

td {{
    border:1px solid #dddddd;
    padding:10px;
}}

.safe {{
    color:green;
    font-weight:bold;
}}

.warning {{
    color:orange;
    font-weight:bold;
}}

.critical {{
    color:red;
    font-weight:bold;
}}

.error {{
    color:#B71C1C;
    font-weight:bold;
}}

</style>

</head>

<body>

<div class="container">

<h2>SSL Certificate Monitoring Report</h2>

<p><b>Date :</b> {today}</p>

<table>

<tr>

<th>Category</th>

<th>Count</th>

</tr>

<tr>

<td>Total Websites</td>

<td>{total_websites}</td>

</tr>

<tr>

<td>SAFE Certificates</td>

<td class="safe">{safe_count}</td>

</tr>

<tr>

<td>WARNING Certificates</td>

<td class="warning">{warning_count}</td>

</tr>

<tr>

<td>CRITICAL Certificates</td>

<td class="critical">{critical_count}</td>

</tr>

<tr>

<td>ERROR Websites</td>

<td class="error">{error_count}</td>

</tr>

</table>

<br>

<p>
Please find the attached SSL Certificate Report.
</p>

<br>

Regards,

<br>

<b>{project_name}</b>

</div>

</body>

</html>
"""

    # ==========================================================
    # SEND EMAIL
    # ==========================================================

    logger.info("Preparing Email Notification...")

    send_email(

        to_emails=to_emails,

        cc_emails=cc_emails,

        bcc_emails=bcc_emails,

        subject=subject,

        body=body,

        attachment_path=csv_report

    )

    logger.info("Email Sent Successfully")

    # ==========================================================
    # PROJECT COMPLETED
    # ==========================================================

    end_time = datetime.now()

    scan_duration = end_time - start_time

    logger.info("=" * 70)
    logger.info("SSL Monitoring Completed Successfully")
    logger.info("=" * 70)

    logger.info(f"Start Time : {start_time}")
    logger.info(f"End Time   : {end_time}")
    logger.info(f"Duration   : {scan_duration}")

    logger.info("=" * 70)

    print("\n")
    print("=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print(f"Scan Started : {start_time}")

    print(f"Scan Ended   : {end_time}")

    print(f"Duration     : {scan_duration}")

    print()

    print(f"CSV Report   : {csv_report}")

    print(f"HTML Report  : {html_report}")

    print()

    print("Email Notification Sent Successfully")

    print("=" * 70)


# ==========================================================
# PROGRAM START
# ==========================================================

if __name__ == "__main__":
    main()