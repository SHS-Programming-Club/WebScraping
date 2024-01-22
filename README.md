# Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/SHS-Programming-Club/WebScraping.git
    ```

2. Change to the project directory:

    ```bash
    cd WebScraping
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

# Flask Password Validation

This is a simple Flask application that serves an HTML page asking the user to enter a password.

1. Run the Flask application:

    ```bash
    python server.py
    ```

    This will startup the website.

7. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to interact with the password form.

## Task

Explore the website to understand how the password validation works. Try to find if there is any way that you can determine the password by programming something in `hack.py`. (Hint: Chrome DevTools)

*You should not need to import any additional packages*

# BeautifulSoup

1. Go to the Main Page of [Wikipedia](https://en.wikipedia.org/wiki/Main_Page). Look around the page.

2. Use BeautifulSoup in `soup.py` to scrape the description of the featured article.