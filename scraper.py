from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import argparse

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Replace this with the correct path to your chromedriver.exe
    service = Service(r'C:\Users\Bibek Paudel\Downloads\chromedriver-win64\chromedriver.exe')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def login_facebook(driver, email, password):
    print("Logging into Facebook...")
    driver.get("https://www.facebook.com/")

    # Wait for the login fields to be available and fill them in
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()

    # Wait until the user is logged in by checking for the presence of the profile icon
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Your profile"]'))
    )
    print("Logged in successfully.")

def navigate_to_page(driver, page_name):
    print(f"Navigating to Facebook page: {page_name}")
    driver.get(f"https://www.facebook.com/{page_name}")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

def scrape_posts(driver, num_posts=5):
    print("Starting to scrape posts...")
    posts_data = []

    # Scroll to load initial posts
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    while len(posts_data) < num_posts:
        try:
            # Ensure we are on the page with posts
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[@role="feed"]')))

            # Fetch posts
            posts = driver.find_elements(By.XPATH, '//div[@role="article"]')
            print(f"Found {len(posts)} posts")
            for post in posts:
                if len(posts_data) >= num_posts:
                    break
                try:
                    # Updated XPath for post text
                    post_text_element = post.find_element(By.XPATH, './/div[contains(@data-ad-preview="message")]')
                    post_text = post_text_element.text
                    post_link = post.find_element(By.XPATH, './/a[contains(@href, "/posts/")]').get_attribute('href')
                    posts_data.append({"text": post_text, "link": post_link})
                    print(f"Post: {post_text}")
                except Exception as e:
                    print(f"Error scraping post: {e}")

            # Scroll down to load more posts
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

        except Exception as e:
            print(f"Error while scraping posts: {e}")
            break

    return posts_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("page_name", help="Facebook page name to scrape posts from")
    parser.add_argument("email", help="Facebook login email")
    parser.add_argument("password", help="Facebook login password")
    parser.add_argument("--num_posts", type=int, default=5, help="Number of posts to scrape")
    args = parser.parse_args()

    driver = setup_driver()

    login_facebook(driver, args.email, args.password)

    navigate_to_page(driver, args.page_name)

    posts_data = scrape_posts(driver, args.num_posts)
    print(f"Scraped {len(posts_data)} posts.")
    for post in posts_data:
        print(f"Post Text: {post['text']}")
        print(f"Post Link: {post['link']}")
        print()

    driver.quit()

if __name__ == "__main__":
    main()