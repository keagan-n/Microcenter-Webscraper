

This script is a Webscraper that uses a URL from Microcenter and grabs all of the items on the page. 
It uses this information to print out the item names and their corresponding prices.
The URL is --> https://www.microcenter.com/search/search_results.aspx?N=4294966937&NTK=all&sortby=match&rpp=96

This page in specific displays the current stock of Video Cards for Desktop Computers.
There are often duplicates of item listings so the program will first prompt for how to handle these cases.
The available responses are "highest" and "lowest" in which the program will print either the highest or lowest price that is available for the item.
Any other response will give an error message and restart the program.