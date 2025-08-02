from examon_core.examon import examon

REPOSITORY = "examon_basic_package"


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics", "Numbers"])
def question():
    return 2 + 1


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics", "Numbers"])
def question():
    return 2 - 1


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics", "Numbers"])
def question():
    return 2 * 2


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics", "Numbers"])
def question():
    return 4 / 2


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", 'Modulo or "Mod" Operator'],
)
def question():
    return 7 % 4


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", 'Modulo or "Mod" Operator'],
)
def question():
    return 50 % 5


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", 'Modulo or "Mod" Operator'],
)
def question():
    return 23 % 2


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", 'Modulo or "Mod" Operator'],
)
def question():
    return 20 % 2


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Powers"],
)
def question():
    return 2**3


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Variables Assignments"],
)
def question():
    a = 5
    return a


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Variables Assignments"],
)
def question():
    a = 5
    return a + a


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Variables Assignments"],
)
def question():
    a = 5
    return a + a - a


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics"])
def question():
    a = 5
    return type(a)


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics"])
def question():
    a = 31.1
    return type(a)


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics"])
def question():
    my_income = 1000
    tax_rate = 0.1
    my_taxes = my_income * tax_rate
    return my_taxes


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics"])
def question():
    return "Hello"


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics"])
def question():
    return "World"


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics"])
def question():
    return "hello \t world"


@examon(repository=REPOSITORY, tags=["Python Data & Structure Basics"])
def question():
    return len("hello")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[0]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return type(mystring)


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[8]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[9]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[-2]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[2:]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[:3]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[3:6]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[1:3]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[::]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[::2]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[2:7:2]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Indexing and Slicing with Strings"],
)
def question():
    mystring = "Hello World"
    return mystring[::-1]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    name = "Sam"
    last_letters = name[1:]
    return last_letters


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    name = "Sam"
    last_letters = name[1:]
    return "P" + last_letters


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    x = "Hello World"
    x = x + " it is beautiful outside!"
    return x


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    letter = "Z"
    return letter * 10


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    return "2" + "3"


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    x = "Hello World"
    return x.upper()


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    x = "Hello World"
    return x.upper


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    x = "Hello World"
    return x.lower()


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    x = "Hello World"
    return x.split()


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    x = "Hi this is a string"
    return x.split()


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "String Properties & Methods"],
)
def question():
    x = "Hi this is a string"
    return x.split("i")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Formatting with the .format() method"],
)
def question():
    return "This is a string {}".format("INSERTED")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Formatting with the .format() method"],
)
def question():
    return "The {2} {1} {0}".format("fox", "brown", "quick")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Formatting with the .format() method"],
)
def question():
    return "The {2} {1} {0}".format("fox", "brown", "quick")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Formatting with the .format() method"],
)
def question():
    return "The {0} {0} {0}".format("fox", "brown", "quick")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Formatting with the .format() method"],
)
def question():
    return "The {q} {b} {f}".format(f="fox", b="brown", q="quick")


@examon(
    repository=REPOSITORY,
    tags=[
        "Python Data & Structure Basics",
        'Float formatting follows "{value:width.precision f}"',
    ],
)
def question():
    result = 104.12345
    return "The result was {}".format(result)


@examon(
    repository=REPOSITORY,
    tags=[
        "Python Data & Structure Basics",
        'Float formatting follows "{value:width.precision f}"',
    ],
)
def question():
    result = 104.12345
    return "The result was {r:1.3f}".format(r=result)


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Formatting with the .format() method"],
)
def question():
    name = "Sten"
    return "Hello, his name is {}".format(name)


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Formatting with the .format() method"],
)
def question():
    name = "Sam"
    age = 3
    return f"{name} is {age} years old"


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Lists"],
)
def question():
    my_list = ["String", 12.45, 4]
    return my_list


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Lists"],
)
def question():
    my_list = ["String", 12.45, 4]
    return len(my_list)


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Lists"],
)
def question():
    my_list = ["one", "two", "three"]
    return my_list[0]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Lists"],
)
def question():
    my_list = ["one", "two", "three"]
    return my_list[1:]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Lists"],
)
def question():
    my_list = ["one", "two", "three"]
    another_list = ["four", "five"]
    return my_list + another_list


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Lists"],
)
def question():
    my_list = ["one", "two", "three"]
    another_list = ["four", "five"]
    new_list = my_list + another_list
    ["one", "two", "three", "four", "five"]
    new_list[0] = "ONE ALL CAPS"
    return new_list


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Lists"],
)
def question():
    my_list = ["one", "two", "three"]
    my_list.append("six")
    return my_list


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    my_dict = {"key1": "value1", "key2": "value2"}
    return my_dict


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    my_dict = {"key1": "value1", "key2": "value2"}
    return my_dict["key1"]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    prices_lookup = {"apple": "2.99", "oranges": "2.50", "durian": "4.99"}
    return prices_lookup["durian"]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
    return d["k2"][2]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
    return d["k2"][2]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
    return d["k3"]["insideKey"]


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"key1": ["a", "b", "c"]}
    my_list = d["key1"]
    return my_list


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"key1": ["a", "b", "c"]}
    my_list = d["key1"]
    letter = my_list[2]
    return letter


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"key1": ["a", "b", "c"]}
    my_list = d["key1"]
    letter = my_list[2]
    return letter.upper()


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"k1": 100, "k2": 200}
    d["k3"] = 300
    return d


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"k1": 100, "k2": 200}
    d["k1"] = "NEW VALUES"
    return d

@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"k1": 100, "k2": 200, "k3": 300}
    return d.keys()


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Dictionaries"],
)
def question():
    d = {"k1": 100, "k2": 200, "k3": 300}
    return d.values()


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Tuples"],
)
def question():
    t = (1, 2, 3)
    return type(t)

@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Tuples"],
)
def question():
    t = ("one", 2)
    return t[0]

@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Tuples"],
)
def question():
    t = ("a", "a", "b")
    return t.count("a")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Tuples"],
)
def question():
    t = ("a", "a", "b")
    return t.index("a")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Tuples"],
)
def question():
    t = ("a", "a", "b")
    return t.index("b")


@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Sets"],
)
def question():
    myset = set()
    myset.add(1)
    myset.add(1)
    return myset

@examon(
    repository=REPOSITORY,
    tags=["Python Data & Structure Basics", "Sets"],
)
def question():
    mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    return set(mylist)

@examon(repository=REPOSITORY, tags=["hello"])
def question():
    return "Hello World"


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "Foo"
    return f"Hello {name}"


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "Bar"
    if name == "Bar":
        return f"Hello {name}"
    return f"Hello"

@examon(repository=REPOSITORY, tags=["Booleans"])
def question():
    return 1 > 2


@examon(repository=REPOSITORY, tags=["Booleans"])
def question():
    return 1 == 2


@examon(repository=REPOSITORY, tags=["Booleans"])
def question():
    return 1 == 1

@examon(repository=REPOSITORY, tags=["Booleans"])
def question():
    return type(True)


@examon(repository=REPOSITORY, tags=["Booleans"])
def question():
    return type(1 == 1)


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "Alice"
    if name == "Bob":
        return f"Hello {name}"
    else:
        return f"Hello"


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "Alice"
    if name == "Bob" or name == "Alice":
        return f"Hello {name}"
    else:
        return f"Hello"


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "Foo"
    if name == "Bar" or name == "Foo":
        return f"Hello {name}"
    elif name == "Alice":
        return f"Hello"

    return f"Hello"


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "Alice or Bob"
    if name == "Bob":
        return f"Hello {name}"
    elif name == "Alice":
        return f"Hello"
    else:
        name = "Charlie"

    return name


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "Alice"
    if name == "Bob" or name == "Alice":
        return f"Hello {name}"
    elif name == "Alice":
        return f"Hello"
    else:
        name = "Charlie"

    return name


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "James"
    if name != "Bob" or name == "Alice":
        return f"Hello {name}"
    elif name == "Alice":
        return f"Hello"
    else:
        name = "Charlie"

    return name


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    name = "James"
    number = 1
    if name != "Bob" or number < 5:
        return f"Hello {name}"

    return name


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    number = 1
    if number > -8 or number < 5 and number <= 1:
        return True

    return False


@examon(repository=REPOSITORY, tags=["hello"])
def question():
    number = 5
    if number > -8 or number < 5 and number <= 1:
        return 1
    elif number > 5:
        return 2
    elif number < 5:
        return 3

    return 4
