# UTSC CSCA20 Course Final Project: A Criminal Record System

By porpose & MacTavish 29

*Notice: Please watch out the system volume when triggering the alarm.*
 
### Why we build this system?
- ~~To earn marks and get GPA 4.0, eventually become a great computer scientist (like Brian) of course!~~

- To show that it is possible for a student in an introductory CS course to build a workable project.

- To enhance our understanding of Python and other programming knowledge.

### Setup of the Program
- Download the source code from [here](https://github.com/porpose/CSCA20_Project/archive/master.zip).

- Install the 3rd party playsound module. You can either follow instructions on its [official website](https://pypi.org/project/playsound/) or run the setup file in the playsound-master folder of our source code.

- Run project.py.

### Basic Functions in the Project
- Ask the user to enter the correct username. Entering unauthorized usernames for more than 3 times will trigger an alarm and the only way to stop it is to restart the program. Entering a blank username is not allowed by the program. The only allowed usernames for now are my partnet's and my utorid which you can actually retrieve from the source code or from our demo video.

- Read the record file. This will display all the data stored in the criminal record file.

- Search for a specific record. Each criminal has an assigned ID. Enter the associated ID for a criminal and the system will show the information of that particular criminal.

- Add a new record. Create a new criminal ID and then enter all the other information such as name, date of birth, crime title, etc. so that the system will write this new record to the existing record file. Blank information will not be accepted by the system.

- Update old records. Enter the ID for a desired criminal record that you would like to change and indicate what modification you want to do. The system will then replace the old record with the new one.

- Remove a record. This will literally remove a record that has the ID that you enter. The system will display the information for that criminal before deleting it.

### Reference
- [This website](https://pypi.org/project/playsound/) provides us with the soundplay module for python, enabling us to play the audio file in our project.

- [This website](https://www.fbi.gov/wanted) provides us with the template data for our record system.

-  This is [the website](https://stackoverflow.com/questions/28277150/write-a-list-in-a-python-csv-file-one-new-row-per-list) where we learned how to tell python to write the information we need into the CSV file.    

### About
- Author: porpose
- Email: porpose@outlook.com

- Co-author: MacTavish 29
- Email: zou.jintong@mail.utoronto.ca

- Project start date: 2019-11-12
- Finish date of the major part of the project: 2019-11-26

- [Click here](https://youtu.be/U3eLtnzCwKk) to view the demonstration video of the program.


