# INET4031 Add Users Script and User List

## 📄 Program Description

This Python script automates the creation of Linux user accounts and group assignments based on structured input from a file. It is designed for system administrators or students in INET4031 to efficiently manage bulk user creation while maintaining control over password assignment and group membership.

📁 Files Included
create-users.py — Main Python script for processing and creating users.

create-users.input — Input file containing user data in the format:

makefile
Copy code
username:password:last_name:first_name:group1,group2

🔧 Features
Reads user data from standard input.

Skips invalid or commented lines.

Creates users with home directories and optional group assignments.

Sets user passwords.

Adds users to one or more groups.

---

## ⚙️ Program User Operation

This script is run from the terminal and reads user account data from a structured input file. Each line of the input corresponds to one user account, and the script interprets the fields to create the account, set the password, and assign any specified groups.

The script is well-commented, so users can look inside for implementation details if needed.

---

### 📥 Input File Format

Each line in the input file should follow this format:


#### Field Descriptions:
- **username** – The Linux username to be created
- **password** – The initial password for the account
- **Full Name** – User's full name (displayed in `finger` or `chfn`)
- **Room Number** – Office or room number
- **Work Phone** – Work contact number
- **Home Phone** – Home contact number
- **Other Info** – Any additional information
- **group1,group2,...** – *(Optional)* Comma-separated list of additional groups for the user

#### Notes:
- To **skip a line**, begin it with a `#` — this marks it as a comment.
- To **skip group membership**, leave the final field empty (end with a colon).

---

🧪 Dry Run Instructions
To test the script without modifying your system:

Comment out the 3 os.system(cmd) lines in the script.

Run:

bash
Copy code
./create-users.py < create-users.input
This will print the commands that would have been run, without actually making changes.

✅ Execution Instructions (Live Run)
⚠️ Only perform these steps once the dry run is successful.

Make the script executable:

bash
Copy code
chmod +x create-users.py
Run the script with elevated permissions:

bash
Copy code
sudo ./create-users.py < create-users.input

---

📌 Notes
Lines in create-users.input starting with # or missing any of the 5 required fields are skipped.

Input lines with - in the group field mean no groups should be assigned.

Groups will be created if they do not already exist (by default behavior of adduser).

---

🕵️‍♂️ Verification
To verify user and group creation:

bash
Copy code
grep user0 /etc/passwd    # Shows user account details
grep user0 /etc/group     # Shows group memberships
