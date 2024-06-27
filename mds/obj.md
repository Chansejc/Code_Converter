QXX
# To-dos
- Strikethrough => ~~{information}~~ 
---

## Core Endpoints
- ~~How to access cached files that have been saved on the server-side?~~
- ~~Building database containing file locations for users files.~~ 
- ~~Where does the relation between the databases meet?~~
- Maximum size for inputs from users
---

## Accounts Endpoints
- ~~What will the relational database structure look like?~~
- Find a way to send E-mails to verify user account removal.
---

## Logistical
- What does the pay model look like? 
---

## Ideal-Functionality
- The User-Accounts database relates to other dbs by the unique UserIDs made upon creating a user.
- Potential table could house "Records Of Entries".
> Each query to save a file/folder will be saved into the ROE. The ROE database will be query-able for the server [Each time a user views their profile a query is made to the ROE then is cached for some time].
> For now we will focus solely on **saving and processing SINGLE FILES**.
---

## Practicality
### The ROE database.
> An entry should contain:
> Entry-id (Unique, Int), User-ID (Non-nullable, String), File-Id (String, Unique, Non-nullable)
- ~~The File-Id should contain information related to the location in which the file is held on the server. So that we can save indivual folders when backing up data instead of a lump some of data to back up at once.~~

### Caching Mechanism on the server-side.
> Saving a list of Folder objects that contain files correlated with the User's ID &/ User's E-mail.
> Queryable from the Client-Side but taking up less computation.


