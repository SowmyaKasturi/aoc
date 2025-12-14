
def read_file(filepath):
    if not filepath:
        print("No file path provided")
    try:
        with open(filepath, "r") as fp:
            data = fp.read()
            for i in data.split("\n"):
                yield i
    except (PermissionError, FileNotFoundError ) as e:
        raise e.strerror