#!/usr/bin/env python3
"""
Helper script to generate database migrations.
"""
import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_migration.py <migration_message>")
        sys.exit(1)
        
    message = sys.argv[1]
    command = ["alembic", "revision", "--autogenerate", "-m", message]
    
    print(f"Running: {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("Migration generated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error generating migration:\n{e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
