
def concatenate():
    inputs=str(input())
    splitting=inputs.split(" ")
    return (("-").join(splitting))

print(concatenate())


def concatenates(*args):
        return (("-").join(args))

print(concatenates("We","all","love","Python!"))