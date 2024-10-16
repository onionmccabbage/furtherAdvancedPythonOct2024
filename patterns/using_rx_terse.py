from reactivex import of
if __name__ == '__main__':
    source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

    source.subscribe(
        on_next = lambda i: print("Received {0}".format(i)),
        on_error = lambda e: print("Error Occurred: {0}".format(e)),
        on_completed = lambda: print("Done!"),
    )