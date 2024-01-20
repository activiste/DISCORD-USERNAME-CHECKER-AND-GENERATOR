# Discord Username Checker and Generator | 100% WORKING ! 👑

## Description 📜

This tool allows you to check the availability of Discord usernames and generate new ones using proxies. It leverages the Proxyscrape service for proxy support. Follow the instructions below to set up and use the tool.

Probably the best checker of 2024. 😏

## Prerequisites 📁 

1. Create an account on [Proxyscrape Dashboard](https://dashboard.proxyscrape.com/sign-up).
2. After signing up, navigate to the "IP Authentication" category on the dashboard and authenticate your IP for proxy access.
3. Wait for 10-15 minutes for the changes to take effect.
4. Go to the "Proxy List" section on the dashboard, download your proxy list, and include it in a file named `proxies.txt`.

## Usage 🛠️

1. Generate Usernames:
   - Use the `gen.py` script to generate usernames.
   - Modify the `numbers` variable in the script to set the desired number of usernames to generate.
     ```python
     # Example:
     numbers = 100
     ```

2. Run the Username Checker:
   - Execute the `checker.py` script.
   - Valid usernames will be saved in the `valid.txt` file.

## Important Notes 📝 

- It is recommended to generate usernames in an amount equivalent to the number of proxies (e.g., 100 usernames for 100 proxies).
- Ensure that you have authenticated your IP for proxy access and downloaded the proxy list before running the tool.
- Proxies are essential for avoiding rate limiting and preventing IP blocks during username checking.

## ⚠️ Disclaimer ⚠️

Use this tool responsibly and in accordance with Discord's terms of service. Excessive or misuse of this tool may lead to actions against your Discord account.

## Credits 👤

- Proxyscrape: [https://proxyscrape.com/](https://proxyscrape.com/)

## License ⚖️

This project is licensed under the [MIT License](LICENSE).
