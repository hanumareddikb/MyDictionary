# MyDictionary
This project is Online Dictionary where we can find meaning for our words.

Features are:
- Registeration using Custom User model.
- Login/Logout.
- Search for the meaning of the entered words using an external API, store the word and the meaning in the database, 
   if the user searches for the same word again, show the meaning from the local database, do not call the external API.
- List all the words in the db in a page, sorted in alphabetical order with pagination.
- If the user searches for a word the first time, email the user the word along with its meaning.
