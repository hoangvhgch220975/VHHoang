from string import punctuation


def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s


from string import whitespace


def remove_whitespace(s):
    """Return copy of s with whitespace removed."""
    for c in whitespace:
        if c in s:
            s = s.replace(c, "")
    return s


# from https://www.lipsum.com/feed/html
string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "\
    "Proin sit amet nulla scelerisque, ultrices enim sed, pretium mi. "\
    "Aenean neque orci, maximus quis risus quis, blandit rutrum purus. "\
    "Etiam varius dui eget justo tempor elementum. "\
    "Duis finibus felis a dapibus tincidunt. "\
    "Nam quis dui tempus, tristique tortor a, vehicula odio. "\
    "Sed ac dolor vel augue imperdiet placerat. "\
    "Donec malesuada erat sapien, molestie convallis nisl iaculis a. "\
    "Donec turpis mi, tincidunt at dolor sit amet, pulvinar commodo justo. "\
    "Proin rutrum nisl et sollicitudin tincidunt. "\
    "Maecenas ut diam ac justo consectetur tincidunt. "\
    "Phasellus pulvinar lectus ut orci finibus aliquam. "\
    "Cras sit amet urna laoreet, aliquet ipsum ut, vulputate odio. "\
    "Vestibulum consectetur, tortor et consectetur gravida, dui nulla dapibus mauris, ac dapibus metus neque nec odio. "\
    "Aliquam at molestie ipsum."
print(string)
print(f"character count = {len(string)}")
print(f"   letter count = {len(remove_whitespace(remove_punctuation(string)))}")
print(f"     word count = {len(string.split())}")

print()
input("Press return to continue ...")
