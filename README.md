# Front end dev test
This exercise is meant to test mostly your front-end coding skills.
Your assignment will be evaluated on the quality of your code, the ease of launching your project and how you think about UX as opposed to UI in terms of design in the context of this assignment.

Note: The backend part is optional, though is a great opportunity to showcase your backend skills!

Good luck! :slightly_smiling_face:

# Front-end (React or Angular)
For the front end part, you will build a web page that will display a list of songs and their ratings taken from the JSON file.

- Songs should be listed in a responsive grid. Think mobile!
- Make the ratings editable by making the stars clickable. (doesn’t need to persist on reload)
- Use React or Angular 1/2/4/5 to build the website
- Each line should look like the screenshot (not pixel perfect). Mandatory elements are the Yousician logo, level, title, rating and artist. For other info, or color choice, you have complete freedom.

Bonus:
- Add pagination
- Add filtering by level
- Add song search
- A good look on the frontend will be appreciated

# Backend (Python, MongoDB) - Optional
For the backend part, we would like you to build a Flask API defining the routes listed bellow.
All routes should return a valid json dictionary.
There is no need to do any complex input validation.
The API should use a mongod server that will contain a “songs” collection loaded from the provided file /songs.json.

List of routes to implement:
- GET /songs
 - Returns a list of songs
 - Add possibility to paginate songs.
- GET /songs/avg/difficulty
 - Takes an optional parameter “level” to select only songs from a specific level.
 - Returns the average difficulty for all songs.
- GET /songs/search
 - Takes in parameter a ‘message’ string to search.
 - Return a list of songs. The search should take into account song’s artist and title. The search should be case insensitive.

- POST /songs/rating/song_id
 - Takes in parameter a “song_id” and a “rating”
 - The call should edit the rating of the song. Rating should be between 1 and 5.
 - Return an empty dictionary

Bonus:
- It is good practice to write tests when coding API routes!
