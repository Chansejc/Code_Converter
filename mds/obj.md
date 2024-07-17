###  ------------------------------------
### | Strikethrough => ~~{information}~~ |
###  ------------------------------------
---

# Refactor 1
---
## To-do
- Maximum word-count for inputs
- Lose the Verification/Authentication Step (saves time/can be implemented when usage raises)
- Lose File Input 
- Add character counter and character limit for input 
- Input from FrontEnd is Payload + Language
- Add some sleep time between querys sent from the frontend.
- Track queries sent from the frontend to track usage over time.
---

# Things I Learned to do:
- ~~Building database containing file locations for users files.~~ 
- ~~Where does the relation between the databases meet?~~
- ~~What will the relational database structure look like?~~
- ~~The ROE database.~~

---

# Functionality to Add (Later):
### Logistical
- What does the pay model look like? 
### Accounts Endpoints
- Find a way to send E-mails to verify user account removal.
### Ideal-Functionality
- The User-Accounts database relates to other dbs by the unique UserIDs made upon creating a user.
- Potential table could house "Records Of Entries".
> Each query to save a file/folder will be saved into the ROE. The ROE database will be query-able for the server [Each time a user views their profile a query is made to the ROE then is cached for some time].
> For now we will focus solely on **saving and processing SINGLE FILES**.
- Taking in files from the client-side (Higher Word-Count)
- How to access cached files that have been saved on the server-side?
### Caching Mechanism on the server-side.
> Saving a list of Folder objects that contain files correlated with the User's ID &/ User's E-mail.
> Queryable from the Client-Side but taking up less computation.
---



