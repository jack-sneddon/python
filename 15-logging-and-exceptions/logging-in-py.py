import logging

#
# I can only set basicConfig once.  once set, can't change
#

# by defualt warning and above - so only warning, error and critical will be printed
""" logging.basicConfig(level=logging.DEBUG)

logging.debug("this is a debug statement")
logging.info("this is an info statement")
logging.warning("this is a warning statement")
logging.error("this is an error statement")
logging.critical("this is a critical statement")
 """

# formatting
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info("this is an info statement")
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

# log to a file
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')

# log fields
fname = 'jack'
lname = 'sneddon'
# logging.error('%s raised an error', fname)
logging.error(f'{fname.title()} {lname.title()} raised an error')


