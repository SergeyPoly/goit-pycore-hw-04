def parse_input(user_input: str) -> list:
    cmd, *args = user_input.split()

    return cmd.strip().lower(), *args