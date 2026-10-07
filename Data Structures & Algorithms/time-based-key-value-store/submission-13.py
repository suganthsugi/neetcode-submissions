class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            curr = self.timeMap[key]
            curr[timestamp] = value
        else:
            self.timeMap[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap and timestamp in self.timeMap[key]:
            return self.timeMap[key][timestamp]
        elif key in self.timeMap:
            valids = [x for x in self.timeMap[key].keys() if x<=timestamp]
            if valids==[]:
                return ''
            lastT = max(valids)
            return self.timeMap[key][lastT]
        return ''
