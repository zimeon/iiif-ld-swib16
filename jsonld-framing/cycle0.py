"""Read and dump JSON-LD for a cycle."""
from pyld import jsonld
import json

doc = json.loads("""
{ "@id": "http://example.org/r1",
  "http://example.org/p1":
  { "@id": "http://example.org/r2",
    "http://example.org/p2":
    { "@id": "http://example.org/r3",
      "http://example.org/p3":
      { "@id": "http://example.org/r1" }
    }
  }
}""")

frame = json.loads("""{"http://example.org/p1": {}}""")
framed = jsonld.frame(doc, frame)
print(json.dumps(framed, indent=2, sort_keys=True))
