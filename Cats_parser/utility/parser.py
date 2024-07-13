def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Remove all spaces and new line symbols
                line.strip()
                if line:
                    # Split each line with comma
                    cat_id, cat_name, cat_age = line.split(",")
                    # Creating dictionary with cat info
                    cat_info = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": int(cat_age)
                    }
                    cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"File with the path {path} was not found")
    except ValueError:
        print(f"File with the path {path} has incorrect data")

    return cats_info
