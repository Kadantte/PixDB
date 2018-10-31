from pixdb import PixDB
import json

if __name__ == "__main__":
    db = PixDB()
    db.write(json.dumps({
        "owo": True,
        "dabdab": [{
            ">~<": "nou"
        }]
    }))
    print(json.loads(db.read()))
