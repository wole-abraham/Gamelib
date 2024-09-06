# Not all have been implemented.. stay tuned




** GameLib **
# GameLib Project

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
     

## Project Structure

```plaintext
gamelib/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── layout.html
│
├── app.py
├── config.py
├── requirements.txt
└── README.md

## Later i'll share how i implemented this project

# Screenshots

![Screenshot_2024-09-06_12 40 44](https://github.com/user-attachments/assets/f0406745-7858-4066-b637-2f6cc4011aa4)
![Screenshot_2024-09-06_12 46 36](https://github.com/user-attachments/assets/270e95b7-f3e1-4944-aefa-0e62f35eca79)
![Screenshot_2024-09-05_21 47 39](https://github.com/user-attachments/assets/ae622a03-7efb-4665-9c62-5107974f15a0)

![Screenshot_2024-09-05_21 55 20](https://github.com/user-attachments/assets/ef2680e3-a424-4516-9a52-d14ad0fca126)

