# CS-340-Client-Server-Development
CS 340 Client Server Development portfolio project
## How do you write programs that are maintainable, readable, and adaptable?

I try to keep programs maintainable and readable by separating different responsibilities into organized sections and reusable functions. In Project One, I created the `AnimalShelter` CRUD Python module to handle the database connection and the create, read, update, and delete operations. This allowed the database code to stay separate from the dashboard code. In Project Two, the dashboard could create an instance of the `AnimalShelter` class and use its `read()` method to retrieve the animal records needed for the different rescue filters. This made the dashboard easier to understand because the interface did not need to contain all of the MongoDB connection logic.
One advantage of this approach is that the CRUD module can be reused instead of rewriting the same database operations for every application. The module already contains methods for creating, reading, updating, and deleting records. In the future, I could reuse or adapt this module for another application that needs to interact with MongoDB, such as another dashboard or a program used to manage records.

## How do you approach a problem as a computer scientist?

I approach a problem by first breaking the requirements into smaller parts and figuring out how the data and application need to work together. For the Grazioso Salvare project, I first connected the dashboard to MongoDB using my existing CRUD module. I then worked on the dashboard layout, rescue filters, data table, chart, and map. After that, I created callbacks so that the components would respond to the user's selections.

This project was different from many previous assignments because I was not only writing code to produce one result. I had to think about how several parts of an application worked together and how the client would actually use the dashboard. I also had to troubleshoot situations where the dashboard received empty or `None` values and add checks so the application would remain stable. In future projects, I would continue breaking client requirements into smaller tasks, design the database queries around those requirements, test each component individually, and then test how everything works together.

## What do computer scientists do, and why does it matter?

Computer scientists use programming, data, and problem-solving skills to create systems that help people complete tasks more efficiently and make better decisions. In this project, the dashboard gives Grazioso Salvare a way to search and analyze a large amount of animal shelter data. The rescue filters allow the organization to identify dogs that meet specific breed, sex, and age requirements for different types of rescue training.

The dashboard also provides an interactive data table, a breed distribution chart, and a geolocation map. These tools make the information easier to understand than searching through individual database records manually. Work like this matters because computer scientists can turn large amounts of raw data into useful tools that support real-world decisions. For a company like Grazioso Salvare, this could save time and make it easier to identify potential rescue-training candidates that match their specific needs.
