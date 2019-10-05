#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development

# Put your user name below:
USER= overly1

all: PutCGI PutHTML

PutCGI:
	chmod 757 marvellookup.py
	cp marvellookup.py /usr/lib/cgi-bin/$(USER)_marvellookup.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp marvellookup.html /var/www/html/class/softdev/$(USER)/python/
	cp marvellookup.css /var/www/html/class/softdev/$(USER)/python/
	cp marvellookup.js /var/www/html/class/softdev/$(USER)/python/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(USER)/python/
