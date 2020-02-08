Simple python3 skeleton file for MongoDB / pymongo.

Usage:
```
python3 skeleton.py --uri <MongoDB Connection String>
```

## Getting started

To begin be sure to update the `db` and `collection` variables to reference the correct namespace.

To do some useful work try adding code similar to the following (be sure to update the queries based on the target dataset):

### Simple Query

```
docs = collection.find({ 'foo': 1 })

for doc in docs:
    pprint.pprint(doc)
```

### Simple Aggregation

```
pipeline = [
    { '$match': { 'foo': 1 } }
]

docs = collection.aggregate(pipeline)

for doc in docs:
    pprint.pprint(doc)
```
