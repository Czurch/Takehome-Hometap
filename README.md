# Takehome-Hometap

An intermediary web service that consumes data from an API and makes it available through a custom API endpoint

Steps to run on your system:

Setup For VSCode:
(Ensure you have both python, pip and pipenv installed)

1. run pipenv --env
   -if it responds "No virtualenv has been created for this project"
   -run pipenv install django
2. copy the path for your environment
3. press cmd+shift+p and search "Select Interpreter" and select Enter interpreter path
4. paste in the path and append "/bin/python" ("\Scripts\python" on windows)

To Run the Backend:

1. Navigate to the home directory (Takehome-Hometap)
2. run -> python manage.py runserver
3. Open up localhost:8000 to view reponses

To Test:
-localhost:8000/homedata/property/<address>/<zip> - will return the raw json for the property you enter.
-localhost:8000/homedata/property/<address>/<zip>/sewer - returns the type of sewer the property has
-localhost:8000/homedata/property/<address>/<zip>/sewer/<sewer_type> - returns true or false if the param for sewer_type matches the property's sewage type.

I have left the API call to my Postman Mock Server so you can see the functional version of the code.
Without the authentication parameters, my code will not serve up data from https://api.housecanary.com/v2/property/details?address=123+Main+St&zipcode=94132
If you would like to change this, navigate to Takehome-Hometap/homedata/views.py and modify the fetchHomeDetails() method to point to your housecanary link instead. It should look like:
requests.get('https://api.housecanary.com/v2/property/details?address={addr}&zipcode={zip}'.format(addr = address, zip = zipcode)).json()

Next Steps:
-The first thing I would address with the implementation would be backend validation of the address and zip. The current mock up relies on frontend form validation. The backend should always validate data before moving on and inform the user whether the data is in-fact valid.
-This setup heavily relies on the current naming convention of the API at https://api-docs.housecanary.com/#property-details. If that structure were to change then this implementation would need to be re-written. This could be prevented if we know that the field names for property data will remain uniform across different API's as well as what fields are important to us.
-In the future it should be easy to allow devs to access other fields in the data just using the existing code.
