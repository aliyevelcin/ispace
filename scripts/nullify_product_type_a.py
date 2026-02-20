#!/usr/bin/env python3
import os
import sys

# Ensure the project root is on sys.path so the project package (ispace) can be imported
# This makes the script runnable from the project root or from inside the scripts/ folder.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import django
from django.db import transaction

# Point to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ispace.settings")
#!/usr/bin/env python3
import os
import sys

# Ensure the project root is on sys.path so the project package (ispace) can be imported
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import django
from django.db import transaction, connection

# Point to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ispace.settings")
django.setup()

# This script will set product_type to NULL for Mac rows where product_type_id == 'a'.
# We use a raw SQL UPDATE to avoid Django trying to coerce the FK value to an integer
# (which raises ValueError when the stored value is non-numeric).

def main():
    sql = """
    UPDATE core_mac
    SET product_type_id = NULL
    WHERE product_type_id = 'a';
    """
    with transaction.atomic():
        with connection.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM core_mac WHERE product_type_id = 'a'")
            count = cur.fetchone()[0]
            print(f"Found {count} Mac row(s) with product_type_id='a'.")
            if count:
                cur.execute(sql)
                print(f"Updated {cur.rowcount} row(s) to product_type=NULL.")
            else:
                print("No rows updated.")


if __name__ == '__main__':
    main()
