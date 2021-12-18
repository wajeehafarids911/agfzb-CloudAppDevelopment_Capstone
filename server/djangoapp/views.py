from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
import random
from api.serializers import DealershipRestSerializer, ReviewRestSerializer
from api.models import DealershipRest, ReviewRest
import cloudant
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
def getAbout(request):
    return render(request, 'djangoapp/about.html')

def update_database(request):
    print("Adding objects to DataBase")
    database_output = get_cloudant_database(database_name="dealerships")

    if type(database_output) == cloudant.database.CloudantDatabase:
        print("Database read successfully. Updating Dealerships... Please wait!")
        
        keys_in_dict = database_output.keys(remote=True)
        count_values = 0
        for key_i in keys_in_dict:
            value_i = dict(database_output.get(key_i, remote=True))
            count_values += 1


            serializer_obj = DealershipRestSerializer(data=value_i)
            if serializer_obj.is_valid():
                print("dealerId: ", value_i["_id"])
                try:
                    dealer_obj = DealershipRest.objects.get(_id=value_i["_id"])
                    dealer_obj.delete()
                except:
                    pass
                serializer_obj.save()
            else:
                pass
                # print("Object to be saved is not valid...")
        
        print("Finished updating Dealerships database")
    
    database_output = get_cloudant_database(database_name="reviews")
    if type(database_output) == cloudant.database.CloudantDatabase:
        print("Updating Reviews Database... Please wait!")
        
        keys_in_dict = database_output.keys(remote=True)
        count_values = 0
        for key_i in keys_in_dict:
            value_i = dict(database_output.get(key_i, remote=True))
            count_values += 1
            # print(f"key={key_i}, value={value_i}")


            serializer_obj = ReviewRestSerializer(data=value_i)
            if serializer_obj.is_valid():
                print("Valid review found with dealerId: ", value_i["_id"])
                try:
                    review_obj = ReviewRest.objects.get(_id=value_i["_id"])
                    review_obj.delete()
                except:
                    pass
                serializer_obj.save()
            else:
                print("Review Object to be saved is not valid...")
        
        print("Finished updating Reviews database")

    return render(request, 'djangoapp/about.html')


def get_cloudant_database(database_name):

    login_dict = {
        "COUCH_URL": "https://9a8f2c7b-c8c1-41e1-988e-182c3f5d926f-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY": "YE7undQzSOjWO9FYgY3AIpv7GxGvr9yhL1prUay-HWPv",
        "COUCH_USERNAME": "9a8f2c7b-c8c1-41e1-988e-182c3f5d926f-bluemix"
    }
    try:
        client = Cloudant.iam(
            account_name=login_dict["COUCH_USERNAME"],
            api_key=login_dict["IAM_API_KEY"],
            connect=True,
        )
        dbs_output = client[database_name]
        type_of_dbs_output = type(dbs_output)
        
        return dbs_output

    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"Else statement reached"}

def get_cloudant_database_as_list(database_name):

    login_dict = {
        "COUCH_URL": "https://9a8f2c7b-c8c1-41e1-988e-182c3f5d926f-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY": "YE7undQzSOjWO9FYgY3AIpv7GxGvr9yhL1prUay-HWPv",
        "COUCH_USERNAME": "9a8f2c7b-c8c1-41e1-988e-182c3f5d926f-bluemix"
    }
    try:
        client = Cloudant.iam(
            account_name=login_dict["COUCH_USERNAME"],
            api_key=login_dict["IAM_API_KEY"],
            connect=True,
        )
        database_output = client[database_name]
        type_of_dbs_output = type(database_output)
        dbs_list = []
        if type(database_output) == cloudant.database.CloudantDatabase:
            print("Database read successfully. Updating Dealerships... Please wait!")
        
            keys_in_dict = database_output.keys(remote=True)
            count_values = 0
            for key_i in keys_in_dict:
                value_i = dict(database_output.get(key_i, remote=True))
                dbs_list.append(value_i)

        return dbs_list

    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"Else statement reached"}

def read_data_from_file(filename, database_name, dealer_id=0):
    list_of_data_output = []
    with open(filename) as json_file:
        data = json.load(json_file)
        for p in data[database_name]:

            if database_name == "reviews":
                if p['dealership'] == dealer_id:
                    list_of_data_output.append(p)
            else:
                list_of_data_output.append(p)
    return list_of_data_output
    
# Create a `contact` view to return a static contact page
def getContact(request):
    print("Called getContact...")
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            print("User found and login was performed...")
            # return redirect('djangoapp/about.html')
        return get_dealerships(request)
        
    else:
        return render(request, 'djangoapp/user_login.html', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return get_dealerships(request)

def register_user(request):
    context = {}
    # If it is a POST request
    if request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            # Login the user and redirect to course list page
            login(request, user)
        
        # Return to main page after logging or signing up the user
        return get_dealerships(request)

    else: # If it is a GET request, just render the registration page
        return render(request, 'djangoapp/registration.html', context)


# Update the `get_dealerships` view to render the index page with a list of dealerships
# Testing
def get_dealerships(request):
    database_output = read_data_from_file("dealerships.json", "dealerships")
    context = {"dealership_list" : database_output}
    return render(request, 'djangoapp/index.html', context)


def getStaticPage(request):
    return render(request, 'djangoapp/static.html')

# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    reviews_filtered = read_data_from_file("reviews-full.json", "reviews", dealer_id)

    context = {"reviews_list":reviews_filtered}
    if request.method == "GET":
        return render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    if request.method =="GET":
        pass
