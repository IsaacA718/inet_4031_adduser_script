#!/usr/bin/python3

# INET4031
# Isaac Arika
# Date Created: 5/8/25
# Date Last Modified: 5/9/25

# Import necessary modules:
import os     # Used to execute system comman
import re     # Used for regular expressions (e.g., checking for comment lines)
import sys    # Used to read input from stdin

def main():
    for line in sys.stdin:
        # Skip lines starting with '#' — these are comments in the input file
        match = re.match("^#", line)

        # Remove whitespace and split the line into fields using ':'
        fields = line.strip().split(':')

        # Skip the line if it's a comment or doesn't have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user details from the input fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Full name in format "First Last"

        # Get a list of groups (can be multiple, separated by commas)
        groups = fields[4].split(',')

        # Simulate account creation
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # print(cmd)
        os.system(cmd)

        # Simulate setting the user's password
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # print(cmd)
        os.system(cmd)

        # Simulate assigning user to groups
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
