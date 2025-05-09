#!/usr/bin/python3

import os
import re
import sys

def main():
    dry_run_input = input("Would you like to run this in dry-run mode? (Y/N): ").strip().upper()
    dry_run = (dry_run_input == 'Y')

    for line in sys.stdin:
        match = re.match("^#", line)
        fields = line.strip().split(':')

        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print(f"Dry-run: Line skipped (commented out): {line.strip()}")
                elif len(fields) != 5:
                    print(f"Dry-run: Line skipped (not enough fields): {line.strip()}")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        if dry_run:
            print(f"Dry-run: Would run -> {cmd}")
        else:
            os.system(cmd)

        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        if dry_run:
            print(f"Dry-run: Would run -> {cmd}")
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run:
                    print(f"Dry-run: Would run -> {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
