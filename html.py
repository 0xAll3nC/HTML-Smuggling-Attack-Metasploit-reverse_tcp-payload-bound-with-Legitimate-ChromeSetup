import re

# Define the paths to the input and output files
b64_file_path = 'payload.b64'
html_file_path = 'test.html'
output_file_path = 'output_test.html'

# Read the base64 string from the payload.b64 file
with open(b64_file_path, 'r') as b64_file:
    base64_string = b64_file.read().strip()

# Read the contents of the test.html file
with open(html_file_path, 'r') as html_file:
    html_content = html_file.read()

# Replace the placeholder with the actual base64 string
new_html_content = re.sub(
    r"var fileData = '.*?';",
    f"var fileData = '{base64_string}';",
    html_content
)

# Write the updated content to a new HTML file
with open(output_file_path, 'w') as output_file:
    output_file.write(new_html_content)

print(f"Base64 string inserted and saved to {output_file_path}")


