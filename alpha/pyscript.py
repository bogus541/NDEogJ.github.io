from browser import ajax
from browser import document as doc
from browser import html, window


def parse():
    global vorc
    try:
        vorc = doc.query["vorc"]
    except KeyError:
        vorc = None
    print(f"VorC  -- {vorc}")
    global q
    try:
        q = doc.query["q"]
    except KeyError:
        q = None
    print(f"Q     -- {q}")
    global order
    try:
        order = doc.query["order"]
    except KeyError:
        order = None
    print(f"Order -- {order}")
    global cid
    try:
        cid = doc.query["cid"]
    except KeyError:
        cid = None
    print(f"Cid   -- {cid}")


def run():
    parse()
