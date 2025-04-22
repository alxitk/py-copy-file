def copy_file(command: str):
    if command.split()[-1] != command.split()[-2]:
        with open(command.split()[-2], "r") as file_in, open(command.split()[-1], "w") as file_out:
            content = file_in.read()
            file_out.write(content)
