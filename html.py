{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 pythonCopy code\
import re\
\
# Define the paths to the input and output files\
b64_file_path = 'payload.b64'\
html_file_path = 'test.html'\
output_file_path = 'output_test.html'\
\
# Read the base64 string from the payload.b64 file\
with open(b64_file_path, 'r') as b64_file:\
    base64_string = b64_file.read().strip()\
\
# Read the contents of the test.html file\
with open(html_file_path, 'r') as html_file:\
    html_content = html_file.read()\
\
# Replace the placeholder with the actual base64 string\
new_html_content = re.sub(\
    r"var fileData = '.*?';",\
    f"var fileData = '\{base64_string\}';",\
    html_content\
)\
\
# Write the updated content to a new HTML file\
with open(output_file_path, 'w') as output_file:\
    output_file.write(new_html_content)\
\
print(f"Base64 string inserted and saved to \{output_file_path\}")\
\
\
}