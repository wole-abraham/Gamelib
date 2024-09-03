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

