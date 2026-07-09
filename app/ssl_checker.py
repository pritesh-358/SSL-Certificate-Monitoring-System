from pathlib import Path

def read_websites():
    # Project root folder ka path nikalo
    project_root = Path(__file__).parent.parent

    # websites.txt ka full path
    website_file = project_root / "websites.txt"

    websites = []

    with open(website_file, "r") as file:
        for line in file:
            website = line.strip()

            if website:
                websites.append(website)

    return websites