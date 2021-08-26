Work Tracker (notes)

•	Research

-	~1 hour of researching both topics to prepare. Initial research which included looking into PostgreSQL which didn’t require much due to the similarity to MySQL, doing some initial search on whether implementing an API in python would be more troublesome then just focusing on a simple implementation in NodeJS. Deciding to use Flask in python to attempt and implementation.


•	Backend

PostgreSQL DB implementation - 

-	~1 hour, organizing it in a manor that made sense to me and allowed for all the variables in the requirement. Implementing and changing to serial keys was a bit trickier than when using MySQL but with proper queries it worked out in the end. Something that would have saved time if I had known the terminology change ahead of time. This was the time taken for the initial setup for backend use, having two tables with the landing_pages table having a foreign key referring to the user that it is owned by.

-   ~30 min, debugging and changing of tables, inserting data to query, organizing a query sheet which has been used for multiple tests, figuring out the port since i decided to not go with the default option.

Python REST API implementation - 

-	(~30 min) Setup Flask environment with python - debugging took 30 min to work out and run successfully as I am getting used to python workstation and setting up modules with it. *Environment path errors mainly

-   ~45 min, setting up the initial route and getting the first get request, returning the list of customers from the customer table. Some minor issues with type converting to be able to print out the result of the query, making it more complex by first going with json type and conversions when a simple str() of the results did the trick.

-   ~15 min, reproducing the get requests to multiple functions, just simply returning the lists as strings which can be converted by the frontend, or sent via different formats

-   ~1 hour, POST methods with basic data type verification, time extended due to a type error when parsing the data from postman, this was due to importing two modules for request which went unnoticed for a while. After the error was spotted the request went through without issue and the post method to add a user was verified.

•	Full-Stack

