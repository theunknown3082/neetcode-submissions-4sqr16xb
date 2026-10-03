class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res, val = "", self.keystore.get(key, [])
        l, r = 0, len(val) - 1
        while l <= r:
            m = l + (r - l) // 2
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
