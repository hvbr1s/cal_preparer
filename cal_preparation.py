def process_row(row):
    elements = row.split(" | ")

    # Check if there are enough elements to remove
    if len(elements) >= 4:
        del elements[2]
        del elements[-1]

    new_row = " | ".join(elements)
    return new_row

def contains_delisted(row):
    return 'delisted' in row.lower()

def generate_html_content(rows):
    html_rows = "\n".join([f"<li>{row}</li>" for row in rows])
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Supported Crypto Cois and Tokens in Ledger Live.</title>
</head>
<body>
  <ul>
    {html_rows}
  </ul>
</body>
</html>"""

    return html_content

def save_to_files(filename, content, mode="w"):
    with open(filename, mode) as file:
        file.write(content)

with open("/home/dan/zendesk_backup/input_cal.txt", "r") as input_file:
    input_list = input_file.readlines()

output_list = [process_row(row.strip()) for row in input_list if not contains_delisted(row.strip())]

# Save output to cal.txt
save_to_files("cal.txt", "\n".join(output_list))

# Generate and save output to cal.html
html_content = generate_html_content(output_list)
save_to_files("cal.html", html_content)
