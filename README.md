# INET4031 Add Users Script and User List

## 📄 Program Description

This program provides an automated solution for Linux system administrators to add multiple users efficiently using a structured input file. Instead of manually running multiple commands like `adduser`, `passwd`, and `usermod`, this Python script streamlines the entire process, ensuring consistency and reducing the chance of human error.

Normally, administrators would use commands such as:
- `adduser username`
- Provide password and additional user details (Full Name, Room Number, etc.)
- `usermod -aG groupname username` to assign group membership

This script automates all of those actions using Python's `subprocess` module to call the same commands programmatically.

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

### 🖥️ Command Execution

1. Ensure the script is executable:
   ```bash
   chmod +x create-users.py
