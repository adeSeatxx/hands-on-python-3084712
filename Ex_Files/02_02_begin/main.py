greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "Ade"

print(name.lower, "Bill")
intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted, "and some more")
print(formatted.lower())
print(formatted.upper())
print(formatted.replace("Ade", "Bill"))
