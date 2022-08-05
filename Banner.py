class BannerString:
    def __init__(self, string="", size=0):
        self.lines = ["" for _ in range(size)]
        if string:
            lines = string.split("\n")
            self.lines[len(self.lines)-1 - len(lines)-1:len(self.lines)-1] = string.split("\n")

    def __add__(self, other):
        res = ''
        if isinstance(other, BannerString):
            length = max(list(map(lambda x: len(x), self.lines)))
            for i, line in enumerate(other.lines):
                res += self.lines[i] + " " * (length - len(self.lines[i])) + line + "\n"
        return BannerString(res)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "\n".join(self.lines)


class Banner:
    __letters = []

    @classmethod
    def from_string(cls, string):
        string = string.replace(" ", "_").lower()
        for letter in string:
            letter = letter.replace("_", "space")
            with open("alphabet/" + letter, "r") as file:
                l = file.read().strip("\n").strip("%")
            cls.__letters.append(BannerString(l, size=10))
        res = BannerString(size=10)
        for i in cls.__letters:
            res += i

        return str(res)