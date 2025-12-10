import os
import shutil
import re
import requests

print("===== TASK AUTOMATION PROGRAM =====")
print("Choose a task:")
print("1. Move all .ipq files to another folder")
print("2. Extract all email addresses from a .txt file")
print("3. Scrape the title of a webpage and save it")
choice = input("Enter your choice (1/2/3): ")

# ---------------------------------------------
# OPTION 1: Move all .ipq files
# ---------------------------------------------
if choice == "1":
    source_folder = input("Enter source folder path: ")
    destination_folder = input("Enter destination folder path: ")

    os.makedirs(destination_folder, exist_ok=True)

    count = 0
    for file in os.listdir(source_folder):
        if file.endswith(".ipq"):
            shutil.move(os.path.join(source_folder, file),
                        os.path.join(destination_folder, file))
            print("Moved:", file)
            count += 1

    print(f"✔ Completed! Moved {count} .ipq files.")

# ---------------------------------------------
# OPTION 2: Extract Emails
# ---------------------------------------------
elif choice == "2":
    input_file = input("Enter input .txt file: ")
    output_file = input("Enter output file name to save emails: ")

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    with open(input_file, "r") as f:
        data = f.read()

    emails = list(set(re.findall(email_pattern, data)))

    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"✔ Extracted {len(emails)} emails and saved in {output_file}")

# ---------------------------------------------
# OPTION 3: Scrape webpage title
# ---------------------------------------------
elif choice == "3":
    url = input("Enter webpage URL: ")

    response = requests.get(url)
    html = response.text

    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)

    if match:
        title = match.group(1)

        with open("web_title.txt", "w") as f:
            f.write("Webpage Title:\n")
            f.write(title)

        print("✔ Title extracted and saved in web_title.txt")
    else:
        print("❌ Title not found on webpage")

# ---------------------------------------------
# Invalid Option
# ---------------------------------------------
else:
    print("❌ Invalid choice! Please run again.")

print("\n===== Program Finished =====")
