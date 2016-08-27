Python Version: 3.5.2
Libraries used: BeautifulSoup, datetime, random, requests, webbrowser

Interacting with the program: 
1.	To launch the program, please use interactive mode (python3 –i).

2.	When the user launches the program in interactive mode, he or she will be greeted with a welcome screen. The terminal will prompt the user with the following:
Input a seach term for a news article: _

3.	The user should input a valid search term. Popular valid search terms are in the list below:
a.	World
b.	Technology/Tech
c.	Business
d.	Economy
e.	Environment
f.	Politics
g.	Sports

For a full list, please refer to the end of this file.

4.	Search terms are not case-sensitive. If a user enters “Economy”, “economy”, or “eCoNoMy”, the results will all be the same.

5.	After the user types in the desired search term and hit enter, the program will take the term, find the corresponding URL for the New York Times category page, and pick the headlining article. The user will see a Title and a Description pop up.

6.	The “Title” prompt will have the full title of the headlining article in the given section of the New York Times. The “Description” prompt will have a short summary of the article, to give the user an idea of what the article is about. 

7.	At the bottom of the terminal, the user will see another prompt:
Do you want to read another similar article, search again, open the full article, or see social media posts about this topic?:

8.	The user can now choose to find a similar article, enter a new search term and read about a new topic, read the full article, or see opinions on the topic.



Option 1: Similar Article
9.	If the user types in “similar article” (see the end for a full list of acceptable commands), another “Title” and “Description” prompt will pop up, this time with a new article. The user will once again be given a choice between finding a similar article, entering a new search term, reading the full article, or seeing opinions on the topic.

Option 2: Search Again
10.	If the user types in “search again” (see the end for a full list of acceptable commands), the program will return to the following screen:
Input a seach term for a news article: _

11.	At this point, the user can input a new search term, read about a new article, and begin the whole process again.

Option 3: Full Article
12.	If the user types in “full article” (see the end for a full list of acceptable commands), the article for which the user has read the title and description will be opened in the user’s browser, in a new tab. The user can then read the full article. When the user returns to the terminal, the program will give the user the four choices once again.

Option 4: Social Media
13.	If the user types in “social media” (see the end for a full list of acceptable commands), a twitter page for that article will open, in a new tab. This page will have comments from other people who read the article. Note: some articles do not have a social media post and many have uncensored comments. 

14.	If at any point the user wishes to exit the program, he or she can simply type “exit” or “exit()”. This will bring the user to the Python 3 terminal, outside of the UI. Once here, the user can run functions, etc. To exit, the user must type exit() once again.


Acceptable Search Terms
1.	World
2.	Politics
3.	Business
4.	Technology/Tech
5.	Sports
6.	Africa
7.	Americas
8.	Asia
9.	Europe
10.	Middle East
11.	Markets
12.	Economy
13.	Energy and environment/Environment
14.	Media
15.	Personal Tech
16.	Entrepreneurship

Acceptable Inputs for Another Article
1.	Another
2.	Another article
3.	Similar
4.	Similar article
5.	Another similar article
6.	Read another similar article

Acceptable Inputs for Full Article
1.	Full
2.	Full article
3.	Open
4.	Open in browser
5.	Browser
6.	Open the full article

Acceptable Inputs for Searching Again
1.	Search again
2.	New search
3.	New term
4.	Search new article
5.	New article


Acceptable Inputs for Social Media
1.	Social media
2.	Twitter
3.	Posts
4.	Read social media posts
5.  Read social media posts about this topic