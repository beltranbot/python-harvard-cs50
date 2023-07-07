import re

name = input("What's your name? ").strip()

matches = re.search("^(.+), (.+)$", name)

if matches:
    last, first = matches.groups()
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

