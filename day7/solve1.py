#!/usr/bin/python

from __future__ import annotations


class File:
    def __init__(self, parent: File, text: str) -> None:
        self.parent = parent
        if text.startswith("dir "):
            self.is_dir = True
            self.name = text.split(" ")[1]
            self.size = -1
            self.children = {}
        else:
            spl = text.split(" ")
            self.is_dir = False
            self.size = int(spl[0])
            self.name = spl[1]
            self.children = {}

    def add_child(self, child: File) -> None:
        if not self.is_dir:
            raise BaseException("cannot add child to non-directory")
        if child.name in self.children:
            raise BaseException(f"cannot add child, child with name {child.name} already exists")
        self.children[child.name] = child

    def short_str(self) -> str:
        if self.is_dir:
            return "dir " + self.name
        return f"{self.size} {self.name}"

    def traverse(self, func: callable) -> None:
        func(self)
        if self.is_dir:
            for child in self.children.values():        
                child.traverse(func)
    
    def compute_size(self) -> int:
        if not self.is_dir:
            return self.size
        if self.size >= 0:
            return self.size
        size = 0
        for child in self.children.values():        
            size += child.compute_size()
        self.size = size
        return size


class FileCounter:
    def __init__(self) -> None:
        self.count = 0

    def count_file(self, file: File):
        if not file.is_dir:
            return
        if file.size <= 100000:
            self.count += file.size


def main():
    root = File(None, "dir /")
    current_dir = root
    ls_pending = False
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if ls_pending:
                    if line.startswith("$ "):
                        ls_pending = False
                    else:
                        current_dir.add_child(File(current_dir, line))
                        continue
                if not line.startswith("$ "):
                    raise BaseException("unexpected non-command line")
                line = line[2:]
                if line == "ls":
                    ls_pending = True
                elif line.startswith("cd "):
                    dir = line[3:]
                    if dir == "/":
                        current_dir = root
                    elif dir == "..":
                        current_dir = current_dir.parent
                    else:
                        current_dir = current_dir.children[dir]
                else:
                    raise BaseException("unexpected command")
            except BaseException as e:
                print(f"error on line {i} ({line}): {e}")
                return
    root.compute_size()
    counter = FileCounter()
    root.traverse(counter.count_file)
    print(counter.count)


if __name__ == "__main__":
    main()

