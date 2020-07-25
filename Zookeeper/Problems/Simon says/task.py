def what_to_do(instructions):
    command = "Simon says"
    length = len(command) + 1
    if instructions.startswith(command):
        return "I " + instructions[length:]
    if instructions.endswith(command):
        return "I " + instructions[:-length]
    return "I won't do it!"
