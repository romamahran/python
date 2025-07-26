import json

class Subj:
    def __init__(self, code, name):
        self.code = code
        self.name = name

class Stud:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.subjs = {}

    def add_subj(self, subj):
        if subj.name not in self.subjs:
            self.subjs[subj.name] = None

    def set_grade(self, subj_name, grade):
        if subj_name in self.subjs:
            self.subjs[subj_name] = grade

    def get_gpa(self):
        g = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}
        t = 0
        c = 0
        for v in self.subjs.values():
            if v in g:
                t += g[v]
                c += 1
        return round(t / c, 2) if c else 0

    def __str__(self):
        s = "\n".join([f"{k}: {v}" for k, v in self.subjs.items()])
        return f"ID: {self.id}\nName: {self.name}\nSubjects:\n{s or 'None'}\nGPA: {self.get_gpa()}"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "subjs": self.subjs}

    @staticmethod
    def from_dict(d):
        st = Stud(d["id"], d["name"])
        st.subjs = d["subjs"]
        return st

class Sys:
    def __init__(self):
        self.studs = {}
        self.subjs = {}

    def add_stud(self, id, name):
        self.studs[id] = Stud(id, name)

    def edit_name(self, id, name):
        if id in self.studs:
            self.studs[id].name = name

    def del_stud(self, id):
        if id in self.studs:
            del self.studs[id]

    def add_subj(self, code, name):
        self.subjs[code] = Subj(code, name)

    def enroll(self, id, code):
        if id in self.studs and code in self.subjs:
            self.studs[id].add_subj(self.subjs[code])

    def grade(self, id, subj_name, grade):
        if id in self.studs:
            self.studs[id].set_grade(subj_name, grade)

    def show(self, id):
        if id in self.studs:
            print(self.studs[id])
        else:
            print("Not found.")

    def save(self, fname):
        d = [s.to_dict() for s in self.studs.values()]
        with open(fname, 'w') as f:
            json.dump(d, f)

    def load(self, fname):
        try:
            with open(fname, 'r') as f:
                d = json.load(f)
                for x in d:
                    s = Stud.from_dict(x)
                    self.studs[s.id] = s
        except:
            print("File not found.")

# Test
if __name__ == "__main__":
    s = Sys()
    s.add_subj("1", "Math")
    s.add_subj("2", "Sci")

    s.add_stud("101", "Mariam")
    s.add_stud("102", "Ali")

    s.enroll("101", "1")
    s.enroll("101", "2")
    s.enroll("102", "2")

    s.grade("101", "Math", "A")
    s.grade("101", "Sci", "B")
    s.grade("102", "Sci", "C")

    s.show("101")
    s.show("102")

    s.save("data.txt")
    s.load("data.txt")
