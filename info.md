# Video Game Portfolio Website: Your Gateway to the World of Video Games
![Screenshot_2024-09-17_02 06 05](https://github.com/user-attachments/assets/fa56d0a2-e1bc-401a-a667-6ef913225371)

![Screenshot_2024-09-17_02 07 12](https://github.com/user-attachments/assets/996e811e-7d16-48e6-a02f-599d90c389b4)


## Purpose of the Project
The purpose of this project is to allow video game enthusiasts to explore, organize, and save their favorite games using data retrieved from the RAWG API. Users can create a personalized library of games, browse popular or trending games, and stay updated with the latest gaming information. The project also integrates infinite scrolling and user login for a seamless experience.

## Team Members, Roles, and Timeline
- **Wole Abraham** – Backend Developer (Lead), Database Design, API Integration  

## Target Audience
This project was created for gamers who want a personalized platform to keep track of their favorite games. It’s especially useful for gamers who enjoy discovering new games and want to store their gaming preferences in one place.

## My Focus
My personal focus was on integrating the RAWG API and setting up a robust backend with Flask. I ensured the application could handle dynamic data loading with infinite scrolling and a functional login system to enhance user engagement.

---

## Story Behind the Project
Growing up, I was always drawn to video games. They were my escape, my window into fantastical worlds that were otherwise unreachable. I used to spend hours curating lists of my favorite games, keeping track of release dates, and discussing them with friends. That experience inspired this project: a platform where users could explore, curate, and discuss video games all in one place. My passion for organization and my love for gaming naturally led me to this project, and I wanted to build something that reflects my dedication to both.

---

## Project Achievements
We have successfully built a fully functional video game portfolio site with the following key features:
1. **User Login** – Users can log in and save their favorite games.
2. **Infinite Scrolling** – Game data loads dynamically as the user scrolls through the pages.
3. **API Integration** – The app uses the RAWG API to fetch game details, ensuring up-to-date data.

### Technologies Used:
- **Backend**: Flask, SQLAlchemy  
- **Frontend**: HTML, CSS, JavaScript, Jinja  
- **Database**: MySQL  
- **API**: RAWG API for game data  

For the backend, Flask was chosen for its simplicity and flexibility, allowing rapid development and easy integration with the RAWG API. MySQL was used for the database to store user-specific data like saved games. 

---

## Technical Challenge: Implementing Infinite Scrolling
One of the most challenging aspects of the project was implementing infinite scrolling. Initially, the site loaded all data at once, making the performance sluggish as more games were added. To fix this, I needed to find a way to load data dynamically as users scrolled down the page.

### Situation
The API provided a large dataset, but loading everything at once caused long wait times and negatively impacted user experience.

### Task
I had to find a solution that would allow the site to load additional data only when needed, improving both performance and usability.

### Action
After some research, I decided to implement infinite scrolling by fetching new game data via AJAX as users scrolled. This involved writing JavaScript to detect when the user reached the bottom of the page and sending an asynchronous request to the Flask backend for more data. I had to modify the Flask route to support pagination and ensure the response contained the appropriate amount of data for each request.

### Result
After implementing the solution, the site performed much better, with games loading in batches rather than all at once. The user experience became smoother, and the loading times significantly decreased.

---

## Lessons Learned
This project taught me the importance of optimizing user experience, especially in dynamic applications. I learned how to better handle API data and integrate infinite scrolling. On a personal level, I improved my Flask and JavaScript skills, while also learning how to effectively manage project timelines.

---

## About Me
I’m Wole Abraham, a backend developer passionate about building scalable web applications and working with APIs. I have experience with Python, Flask, SQL, and JavaScript. You can check out my project on GitHub and the live demo below:

- [GitHub Repository](https://github.com/wole-abraham/gamelib)
devwole.pythonanywhere.com
