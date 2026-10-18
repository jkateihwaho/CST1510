"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Return the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print("=" * 34)
    print("  RECORD CHECK  -  " + label)
    print("=" * 34) 
    print("  Used        :", value)
    print("  Total       :", limit)
    print("  Free        :", difference)
    print("  Percent     :", round(percent, 2), "%")
    print("  Status      :", status)
    print("=" * 34)

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
    {"label": "srv-01", "value": 87, "limit": 120},
    {"label": "srv-02", "value": 45, "limit": 100},
    {"label": "srv-03", "value": 130, "limit": 120},
]




# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

"""Looping Over Records"""
over_limit_count = 0

with open("results.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(
            record["value"],
            record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        f.write(record["label"] + "," + status + "\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print("Over limit:", over_limit_count)

with open("results.txt") as f:
    print(f.read())



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
