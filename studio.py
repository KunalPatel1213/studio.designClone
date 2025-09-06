print("---today build a clone---")


class studio:
    def __init__(self, name, working, uses):
        self.name = name
        self.working = working
        self.uses = uses

    def show(self):
        print(f"Name : {self.name}")
        print(f"Working : {self.working}")
        print(f"Uses : {self.uses}")

# ✅ main function ko class ke bahar rakho
def main():
    std = studio("std.design", "createyourdesign", "design your things")
    std.show()

main()