st = input()


def camel_case(st_):
    output = st_.title().split()
    return ''.join([output[0].lower()] + output[1:])


print(camel_case(st))
