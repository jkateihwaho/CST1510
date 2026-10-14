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
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).


def status_of(percent):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Return the difference and percentage for a value and limit."""
    difference = value - limit
    percent = (value / limit) * 100 
    return difference, percent

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

# ==================================================================== INPUT
# 2. Ask for your three values.
#


label = input("Enter a label (or quit): ")
value = float(input("Enter value used: "))
limit = float(input("Enter total limit: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#


difference, percent = check(value, limit)
status = status_of(percent)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    

print_report(label, value, limit, difference, percent, status)



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
