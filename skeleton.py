#!/usr/bin/env python3

import traceback
import argparse
import pymongo
import pprint
# import random

# random.seed(0)

def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--uri", default="localhost:27017", help="MongoDB URI (default: 'localhost:27027')")
    ap.add_argument("-v", default=0, action="count", help="verbose output (add more v's for more verbose output)")

    args = vars(ap.parse_args())

    uri = args["uri"]
    verbose = args["v"]

    try:
        print("Connecting...", end="", flush=True)
        connection = pymongo.MongoClient(uri)
        print("Done")

        # update db & connection variables
        db = connection['test']
        collection = db['collection']

        # TODO: add code here

    except KeyboardInterrupt:
        print("..Exiting")
    except:
        print("..Exception")
        print(traceback.print_exc())

if __name__ == "__main__":
    main()
