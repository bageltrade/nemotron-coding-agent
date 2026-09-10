# authorized testing/education only
try:
    import pynput
    print("pynput available - keylogger functionality would be active")
except ImportError:
    with open("keylog_demo.txt", "w") as f:
        f.write("Mock keylogger output: \\n")
        f.write("Key: a\\n")
        f.write("Key: b\\n")
        f.write("Key: c\\n")