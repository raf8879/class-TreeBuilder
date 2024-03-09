class TreeBuilder:

    def __init__(self):
        self.st = {}
        self.level = 0

    def add(self, item):
        self.st.setdefault(self.level, []).append(item)

    def structure(self):
        if len(self.st) > 0:
            return self.st[0]
        else:
            return []

    def __enter__(self):
        self.st.setdefault(self.level, [])
        self.level += 1

    def __exit__(self, exc_type, exc_value, traceback):
        temp = self.st.get(self.level)
        self.st[self.level] = []
        self.level -= 1
        if len(temp) > 0:
            self.st.setdefault(self.level, []).append(temp)