def hello():
    print("Hello! How are you doing today?")

hello()

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

result = pack(1, 2, 3)
print(result)


def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
        return

    print("First I eat " + lunch_items[0])
    for item in lunch_items[1:]:
        print("Next I eat " + item)

eat_lunch(["sandwich", "apple", "chips"])
eat_lunch([])