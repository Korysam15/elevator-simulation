import argparse

# list to integer
def list2i(s):
    try:
        return list(map(int, s.split(',')))
    except:
        raise argparse.ArgumentError("Must be a comma-separated integer")