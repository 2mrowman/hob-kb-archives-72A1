import os
from urllib.parse import quote

# Ρυθμίσεις
SECTIONS = {
    "Docs": "docs",
    "Libraries": "libraries",
    "Scripts": "scripts"
}
INDEX_FILE = "index.md"

def list_md_files(folder):
    links = []
    for f in sorted(os.listdir(folder)):
        if f.lower().endswith(".md"):
            path = f"./{folder}/{quote(f)}"
            title = f.replace("_", " ").replace("-", " ").replace(".md", "")
            links.append(f"- [{title}]({path})")
    return links

def replace_section(lines, section, new_links):
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith(f"## {section}".lower()):
            start = i
            break
    if start is None:
        return lines
    end = start + 1
    while end < len(lines) and not lines[end].startswith("## "):
        end += 1
    return lines[:start+1] + ["\n"] + new_links + ["\n"] + lines[end:]

def main():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for section, folder in SECTIONS.items():
        if os.path.exists(folder):
            links = list_md_files(folder)
            lines = replace_section(lines, section, links)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("✅ index.md ενημερώθηκε επιτυχώς.")

if __name__ == "__main__":
    main()
