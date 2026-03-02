import logging

def get_logger(name="app"):
    l = logging.getLogger(name)
    if not l.handlers:
        h = logging.StreamHandler()
        l.addHandler(h)
    l.setLevel(logging.INFO)
    return l