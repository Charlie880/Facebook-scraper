
# Facebook Post Scraper

This Python script automates the process of logging into Facebook, navigating to a specific Facebook page, and scraping a specified number of posts from that page. It uses the Selenium library to interact with the web browser.

## Features

- **Headless Mode**: The script runs in headless mode, meaning it doesn't open a visible browser window.
- **Facebook Login**: Automates the login process using your provided Facebook credentials.
- **Page Navigation**: Automatically navigates to the specified Facebook page.
- **Post Scraping**: Scrapes a specified number of posts from the page, including the post text and link.

## Requirements

- Python 3.x
- Selenium (`pip install selenium`)
- ChromeDriver (download the appropriate version for your Chrome browser)

## Setup

1. **Install Selenium**:
    ```bash
    pip install selenium
    ```

2. **Download ChromeDriver**:
   - Download the correct version of ChromeDriver for your Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/).
   - Place the `chromedriver.exe` file in a known directory (e.g., `C:\path\to\chromedriver.exe`).

3. **Modify the Script**:
   - Update the `service = Service(r'C:\path\to\chromedriver.exe')` line in the script with the correct path to your `chromedriver.exe`.

## Usage

To use the script, run it from the command line with the required arguments:

```bash
python facebook_scraper.py <page_name> <email> <password> --num_posts <number_of_posts> [--headless]
```

- **`<page_name>`**: The username or ID of the Facebook page you want to scrape (e.g., `nasa`).
- **`<email>`**: Your Facebook login email.
- **`<password>`**: Your Facebook login password.
- **`--num_posts`**: (Optional) The number of posts you want to scrape. The default is 5.
- **`--headless`**: (Optional) If specified, the script will run in headless mode (no visible browser window).

### Example

To scrape the last 5 posts from NASA's Facebook page without showing the browser window:

```bash
python facebook_scraper.py nasa youremail@example.com yourpassword --num_posts 5 --headless
```

## How It Works

1. **Setup Driver**: The script sets up a headless Chrome browser using Selenium.
2. **Login to Facebook**: It logs into Facebook with the provided credentials.
3. **Navigate to the Page**: The script navigates to the specified Facebook page.
4. **Scrape Posts**: It scrapes the specified number of posts from the page, including the post text and link.
5. **Output**: The scraped posts are printed to the console.

## Troubleshooting

- **Login Issues**: Ensure your credentials are correct. Facebook might flag automated logins; consider using app passwords or two-factor authentication.
- **ChromeDriver Compatibility**: Ensure your ChromeDriver version matches your installed Chrome browser version.

## License

This project is licensed under the MIT License.
