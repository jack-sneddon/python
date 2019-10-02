improve your productivity is to make your scripts as handy and straightforward as possible, especially when you are several developers working on the same project.
In order to achieve that, I advise you to respect 4 guidelines:

1. You should provide default arguments values when possible - how?
	• parse the arguments into a list and traverse the list
    • Use 'argparse' library to simplify the work of building up a command line argument list and parsing through it.
    • Use 'click' library 
	
2. All error cases should be handled (ex: a missing argument, a wrong type, a file not found)

3. All arguments and options have to be documented

4. A progress bar should be printed for not instantaneous tasks
