def get_cats_info(path: str) -> list:
    try:
        cats_info = []

        with open(path, 'r', encoding='utf-8') as file:
              for line in file:
                    try:
                        cat_data = line.strip().split(",")

                        if len(cat_data) == 3:
                            parsed_cat_data = {
                                "id": cat_data[0].strip(),
                                "name": cat_data[1].strip(),
                                "age": cat_data[2].strip(),
                            }
                            cats_info.append(parsed_cat_data)
                        else:
                            print(f"Warning: Missing data in line: {line.strip()}")
                    
                    except ValueError:
                        print(f"Warning: Could not parse line: {line.strip()}")
    

    except FileNotFoundError:
        print("Warning: file not found!")
    except Exception as e:
        print(f"Something else went wrong: {e}")

    return cats_info

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)