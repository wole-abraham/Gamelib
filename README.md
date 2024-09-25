




** GameLib **
# GameLib

## Overview

GameLib is a web application that allows users to explore a vast collection of video games. It utilizes the RAWG API to retrieve game data and provides users with a platform to create their own game library. Users can browse through various games, view detailed descriptions, and add their favorite games to a personalized library.

## Features

- **Game Exploration**: Browse through a comprehensive collection of video games retrieved from the RAWG API.
- **Game Details**: View detailed information about each game, including descriptions, genres, release dates, and more.
- **User Authentication**: Implement user login to allow users to create an account and manage their game library (in progress).
- **Personal Game Library**: Users can add games to their personal library (in progress).
- **Infinite Scrolling**: Dynamically load more games as you scroll down the page.
- **Responsive Design**: The site is built to be fully responsive, providing an optimal viewing experience across devices.
- **Template Customization**: A front-end template has been integrated and customized to work with Flask's Jinja templating.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (with a customized front-end template)
- **API**: RAWG API
- **Database**: No database is currently used; data is retrieved directly from the API.orn
- **Environment**: Python Virtual Environment

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/wole-abraham/gamelib.git
    cd gamelib
    ```

2. **Create and Activate Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    - Create a `.env` file in the root directory and add your RAWG API key:
    ```bash
    RAWG_API_KEY=your_rawg_api_key
    ```

5. **Run the Application**:
    ```bash
    flask run
    ```
   - The application will be available at `http://127.0.0.1:5000` do check the app.py file. 
     



## Screenshots
![Screenshot_2024-09-17_02 07 24](https://github.com/user-attachments/assets/ff7eb24b-5503-4fbc-87fd-e43ddaa25b33)

![Screenshot_2024-09-17_02 07 12](https://github.com/user-attachments/assets/9fbb201c-a09c-43ca-b6b6-980bc81f2adf)

![Screenshot_2024-09-17_02 07 38](https://github.com/user-attachments/assets/de335f05-68ad-4a18-94fd-ac2aad29c94b)

![Screenshot_2024-09-17_02 07 45](https://github.com/user-attachments/assets/f3895cda-d222-4328-9608-bb04f6e7212a)














