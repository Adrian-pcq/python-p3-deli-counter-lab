def line(line):

    if len(line)==0:
        print("The line is currently empty.")
    else:
        i=1
        persons = []
        for person in line:
            persons.append(f"{i}. {person}")
            i+=1
        a = " ".join(persons)
        print(f"The line is currently: {a}")

def take_a_number(line,person):
    spot = len(line)+1
    line.append(person)
    print(f"Welcome, {person}. You are number {spot} in line.")


def now_serving(line):
    if len(line)==0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {line[0]}.")
        del line[0]