month:str=None

print("Kérem a hónapot")
month=str(input())

match month:
    case "Január":
        print("1")
    case "Február":
        print("2")
    case "Március":
        print("3")
    case "Április":
        print("4")
    case "Május":
        print("5")
    case "Június":
        print("6")
    case "Július":
        print("7")
    case "Augusztus":
        print("8")
    case "Szeptember":
        print("9")
    case "Október":
        print("10")
    case "November":
        print("11")
    case "December":
        print("12")
    case _:
        print("Nincs ilyen hónap")
