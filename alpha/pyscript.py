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


def GETv():
    req = ajax.ajax()
    req.bind('complete', on_complete)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def starter():
    if vorc == None: return
    if vorc == "v": GETv()
    if vorc == "c": GETc()


def run():
    parse()
    starter()
