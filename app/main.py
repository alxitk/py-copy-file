def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        file_copy = command.split()[-1]
        file_original = command.split()[-2]
        if file_original != file_copy:
            try:
                with (open(file_original, "r") as file_in,
                      open(file_copy, "w") as file_out):
                    content = file_in.read()
                    file_out.write(content)
            except FileNotFoundError as e:
                print(e)
