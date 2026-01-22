# Technical
Technical interview 

HOW TO RUN THE CODE 
- For all analysis, run Technical.ipynb. It was created to function on Collab, directly downloading the data from this repository.
- Run through each cell consecutively to see how analysis was generated. Previous outputs are also present within the file.
- Each analysis should save its own results as a file - original results will be in this repository.
- Open the Dashboards.py file
- Run the command ‘panel serve Dashboard.py’ within your terminal
- If successful you will see a link appear for the dashboard
 *Bokeh app running at: http://localhost:5006/Dashboard
 *Starting Bokeh server with process id: 72034
-Open link to dashboard

SCHEMA EXPLANATION
	It seemed there were two main tables that needed to be created as all attributes could be nicely attributed to one or the other. These two main tables ended up being SAMPLES and SUBJECTS. From here, these two tables needed to be able to be joined despite how many samples a subject may have, hence the SUBJECT_SAMPLE table of the two primary keys to join the two when necessary. Other tables would have been superfluous, so no more tables were created. 
	As this operation is sized up I would have to spend more time planning how to reduce time/computation. Having entire joins, multiple .csv files that are saved/opened, it functions for this set, but it wouldn’t for incredibly large sets. I also may need to consider more tables as new relations may become important with different tests such as cell environment. Lastly, SQLite is good for this, but with larger/more secure sets it may be pertinent to stream them from a database instead of hosting them locally.

OVERVIEW
	I chose to start in google colab as I wanted to use a platform in which everyone is guaranteed (as far as I am aware) to have the same set up, meaning anyone would be able to run it. The start of the code in the Technical.ipynb file downloads the cell_count.csv data and puts it in a dataframe (to check that everything is functioning) and an SQL database (for computation).  The schema for this was the tables samples, subjects, and subject_sample with the last table connecting the first to.
	From here queries in SQL (converted to dataframe as colab cannot visualize straight from SQL) were done to find any answers to what was asked of the analysis. All analyses were done in order and labeled by the sections of the form sheet as I felt that would be the best way to organize it.
	For the dashboard I used the panel python library. I did not want to create the hassle of a standing website server and wanted just a simple widget based way to create the dashboard. Tabs seemed like an easy and clear way to split up the various sections. It is not the prettiest as I ran out of time, but it is functional. 

LINK TO DASHBOARD (after you have started a local server as in the HOW TO RUN CODE section)
http://localhost:5006/Dashboard
