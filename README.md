Interacting with the program: 
To launch the program, please use interactive mode (python3 –i).

When the user launches the program in interactive mode, he or she will be greeted with a welcome screen. The terminal will prompt the user with the following:
Input a search term for a news article: ___

The user should input a valid search term. Popular valid search terms are in the list below:
a.	World
b.	Technology/Tech
c.	Business
d.	Economy
e.	Environment
f.	Politics
g.	Sports

For a full list, please refer to the end of this file.

Search terms are not case-sensitive. If a user enters “Economy”, “economy”, or “eCoNoMy”, the results will all be the same.

After the user types in the desired search term and hit enter, the program will take the term, find the corresponding URL for the New York Times category page, and pick the headlining article. The user will see a Title and a Description pop up.

The “Title” prompt will have the full title of the headlining article in the given section of the New York Times. The “Description” prompt will have a short summary of the article, to give the user an idea of what the article is about. 

At the bottom of the terminal, the user will see another prompt:
Do you want to read another similar article, search again, open the full article, or see social media posts about this topic?:

The user can now choose to find a similar article, enter a new search term and read about a new topic, read the full article, or see opinions on the topic.



Option 1: Similar Article -
If the user types in “similar article” (see the end for a full list of acceptable commands), another “Title” and “Description” prompt will pop up, this time with a new article. The user will once again be given a choice between finding a similar article, entering a new search term, reading the full article, or seeing opinions on the topic.

Option 2: Search Again -
If the user types in “search again” (see the end for a full list of acceptable commands), the program will return to the following screen:
Input a seach term for a news article: _

At this point, the user can input a new search term, read about a new article, and begin the whole process again.

Option 3: Full Article - 
If the user types in “full article” (see the end for a full list of acceptable commands), the article for which the user has read the title and description will be opened in the user’s browser, in a new tab. The user can then read the full article. When the user returns to the terminal, the program will give the user the four choices once again.

Option 4: Social Media - 
If the user types in “social media” (see the end for a full list of acceptable commands), a twitter page for that article will open, in a new tab. This page will have comments from other people who read the article. Note: some articles do not have a social media post and many have uncensored comments. 

If at any point the user wishes to exit the program, he or she can simply type “exit” or “exit()”. This will bring the user to the Python 3 terminal, outside of the UI. Once here, the user can run functions, etc. To exit, the user must type exit() once again.

