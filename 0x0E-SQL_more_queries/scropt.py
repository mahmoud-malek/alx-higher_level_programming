import requests
from bs4 import BeautifulSoup

# URL of the login page
# Replace this with the login URL
login_url = 'https://intranet.alxswe.com/auth/sign_in'
data = {
    'username': 'island.of.professionalism@gmail.com',
    'password': 'Ma01121403041^^^'
    # Add other required fields if necessary
}

# URL of the page with files after login
# Replace this with the desired page URL
page_url = 'https://intranet.alxswe.com/projects/274'

# Create a session to persist the login credentials
with requests.Session() as session:
    # Perform login
    login_response = session.post(login_url, data=data)

    if login_response.status_code == 200:
        # Fetch the protected page after successful login
        page_response = session.get(page_url)

        if page_response.status_code == 200:
            html_content = page_response.text

            # Parse HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find all elements containing file information
            task_divs = soup.find_all('div', attrs={'data-role': 'data-position' : 'id'})
            if task_divs:
                for div in task_divs:
                    # Find all div elements with class="list-group-item" within each task div
                    list_group_items = div.find_all(
                        'div', class_='list-group-item')
                    if list_group_items:
                        for item in list_group_items:
                            # Find the file name within each 'list-group-item' div
                            file_code = item.find('code')
                            if file_code and 'File:' in file_code.text:
                                filename = file_code.text.strip().replace('File:', '')

                                # Create a file with the extracted filename
                                with open(filename, 'w') as file:
                                    file.write(
                                        f"This is a new {filename} file created from HTML content.")
                                    print(
                                        f"File '{filename}' has been created.")
            else:
                print("No 'task' div found in the HTML.")
        else:
            print("Failed to fetch the protected page.")
    else:
        print("Login failed.")
