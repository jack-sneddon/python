def get_formatted_name(first_name, last_name) :
    """Return a full name, neatly formatted """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#
# optional parameters - middle name
#
def get_full_name(first_name, last_name, middle_name = '') :
    """Return a full name, neatly formatted """
    if middle_name :
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()
