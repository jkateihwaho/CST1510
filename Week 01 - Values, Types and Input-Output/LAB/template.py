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

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#


label = input("Enter Label: ")      
first = float(input("Enter first number: "))    
second = float(input("Enter second number: "))     


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#


difference = first - second    
percent = first / second * 100     


# =================================================================== OUTPUT
# 3. Print the report.
#


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)



print("=" * 34)
print(f"  First      : {first:>10.2f}")
print(f"  Second     : {second:>10.2f}")
print(f"  Difference : {difference:>10.2f}")
print(f"  Percent    : {percent:>10.2f} %")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
