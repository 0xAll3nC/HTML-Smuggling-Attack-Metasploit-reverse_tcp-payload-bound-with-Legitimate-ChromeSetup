# HTML-Smuggling-Attack-Metasploit-reverse_tcp-payload-bound-with-Legitimate-ChromeSetup

## Objective
Deliver a Metasploit reverse_tcp payload bound with ChromeSetup.exe through HTML smuggling.

## Prerequisites
- **Kali Linux**: Apache server, Metasploit, `base64`, Python
- **Windows**: PowerShell, SCP client, ChromeSetup.exe, payload.exe
- **Network**: Proper SSH and web access configurations

## Steps
1. **Generate Payload**: Create Metasploit payload using `msfvenom`.
2. **Bind Executables**: Use PowerShell or binding tool to combine ChromeSetup.exe and payload.exe.
3. **Encode Payload**: Convert to base64 and insert into HTML.
4. **Host HTML**: Serve the HTML file via Apache.
5. **Execute Payload**: Download and run from the target machine.

## Disclaimer
For educational purposes only. Use responsibly.
