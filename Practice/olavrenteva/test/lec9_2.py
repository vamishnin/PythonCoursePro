import threading

if __name__ == "__main__":
    ev = threading.Event()
    print(ev.is_set())
    ev.clear()
    print(ev.is_set())
    ev.set()
    print(ev.is_set())
