#
# Description: Connects to Microsoft 365 and performs a content search
# to find and purge a malicious email from all user mailboxes.
# Note: This requires the 'ExchangeOnlineManagement' PowerShell module
# and appropriate permissions in your M365 tenant.
# This is a conceptual script; real-world use requires robust error handling.
#

import subprocess
import sys

# --- Configuration ---
EMAIL_SUBJECT_TO_PURGE = "Urgent: Please Verify Your Account"
M365_ADMIN_USER = "admin@yourtenant.onmicrosoft.com"

def run_powershell_command(command):
    """Executes a PowerShell command and returns the output."""
    try:
        # Using PowerShell Core (pwsh)
        process = subprocess.run(["pwsh", "-Command", command], capture_output=True, text=True, check=True)
        print("Successfully executed command.")
        print(process.stdout)
        return process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing PowerShell command: {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'pwsh' not found. Is PowerShell Core installed and in your PATH?")
        sys.exit(1)


def main():
    """Main function to connect to Exchange Online and purge an email."""
    print("--- Starting Phishing Email Quarantine Script ---")

    # 1. Connect to Exchange Online
    # Note: For automation, use certificate-based authentication instead of interactive login.
    connect_command = f"Connect-ExchangeOnline -UserPrincipalName {M365_ADMIN_USER} -ShowProgress $false"
    print(f"Connecting to Exchange Online as {M365_ADMIN_USER}...")
    run_powershell_command(connect_command)

    # 2. Create a new compliance search to find the email
    search_name = "Phishing_Incident_Search"
    query = f'(Subject:"{EMAIL_SUBJECT_TO_PURGE}")'
    search_command = f"New-ComplianceSearch -Name {search_name} -ExchangeLocation All -ContentMatchQuery '{query}'"
    print(f"Creating compliance search with query: {query}")
    run_powershell_command(search_command)

    # 3. Start the compliance search
    start_search_command = f"Start-ComplianceSearch -Identity {search_name}"
    print("Starting compliance search...")
    run_powershell_command(start_search_command)
    print("Wait for the search to complete in the M365 Compliance Center.")

    # 4. Create a purge action (SoftDelete)
    # Important: In a real incident, you might choose HardDelete.
    # The command requires you to wait until the search is complete.
    purge_command = f'New-ComplianceSearchAction -SearchName "{search_name}" -Purge -PurgeType SoftDelete'
    print("\nTo complete the purge, run the following command in PowerShell after the search is complete:")
    print(purge_command)
    print("\n--- Script Finished ---")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        EMAIL_SUBJECT_TO_PURGE = sys.argv[1]
    main()feat: Add script to quarantine phishing emails.
