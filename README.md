# ProjectDog

How to use:

1. Ensure that you have python installed

 -Available from download on the web and from linux repos of your choice

2. Ensure that you have the scrapy library installed

 -On a ubuntu-based machine, apt-get install python-scrapy
  pip install should also work if you prefer to install it that way

3. From this folder, navigate to sample/spiders/test.py

 -THIS is the main python script to begin everything.
 -In the future, let's call it with ANOTHER script located in the root
 directory of this setup?

4. Run the following command from this folder with the test.py:
 
 "scrapy crawl [script name, in this case 'test'] -o output.csv -t csv
 
 -NOTE ON THE NAME:
  
   Drop the .py file extension. So, test.py becomes test in this command.
