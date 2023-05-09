# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:10:55 2023

@author: SHARJAH LAPTOPS
"""

#Group name:
    #Bug Smashers🦗
    
#Group members:
    # Muzammil Hussain
    # Hafiz Muhammad Jahanzeb Ejaz
    # Ali Haider
    # Muhammad Asfand Kashif
    # Muhammad Furqan Javaid
    # Muhammad Abdullah
    # Muhammad Salman Manzoor

class customers:
    def __init__(self, customer_name, customer_id, customer_number, customer_comments):
       self.customer_name = customer_name
       self.customer_id = customer_id
       self.customer_number = customer_number
       self.customer_comments = customer_comments
    
    def getcustomersDetails(self):
        print(f"customer_name: {self.customer_name}\ncustomer_id: {self.customer_id}\ncustomer_number: {self.customer_number}\ncustomer_comments: {self.customer_comments}\n")
        
class Sculpture_Studio:
    def __init__(self, designer_name, designer_id, Studio_location, Studio_number, customer_name, customer_id, customer_number, customer_comments):
        self.designer_name = designer_name
        self.designer_id = designer_id
        self.Studio_location = Studio_location
        self.Studio_number = Studio_number
        self.customer_obj = customers(customer_name, customer_id, customer_number, customer_comments)
        
    def getSculpture_StudioDetails(self):
        print(f"designer_name: {self.designer_name}\ndesigner_id: {self.designer_id}\nStudio_location: {self.Studio_location}\nStudio_number: {self.Studio_number}\n")
        self.customer_obj.getcustomersDetails()

Sculpture_Studiolist = []
for x in range(3):
    designer_name = input("Enter the designer_name: ")
    designer_id = input("Enter the designer_id: ")
    Studio_location = input("Enter the Studio_location: ")
    Studio_number = input("Enter the Studio_number: ") 
    customer_name = input("Enter the customer_name: ")
    customer_id = input("Enter the customer_id: ")
    customer_number = input("Enter the customer_number: ")
    customer_comments = input("Enter the customer_comments: ")
    Sculpture_Studiolist.append(Sculpture_Studio(designer_name, designer_id, Studio_location, Studio_number, customer_name, customer_id, customer_number, customer_comments))

for Sculpture_Studiolistobj in Sculpture_Studiolist:
    Sculpture_Studiolistobj.getSculpture_StudioDetails()


class SculptureCourse:
    def __init__(self, course_name, course_description, duration, level, price):
        self.course_name = course_name
        self.course_description = course_description
        self.duration = duration
        self.level = level
        self.price = price
    
    def getCourseDetails(self):
        print(f"Course Name: {self.course_name}\nDescription: {self.course_description}\nDuration: {self.duration} hours\nLevel: {self.level}\nPrice: {self.price} RS\n")
    def registeringcourse(self):
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        # Store this information in a list or database for future reference
        registration_data = [name, email, phone, address, self.course_name]
        print("Registration successful!")
        print(registration_data)
class SculptureProduct:
    def __init__(self, product_name, product_num, product_description, product_price):
        self.product_name = product_name
        self.product_num = product_num
        self.product_description = product_description
        self.product_price = product_price
    
    def getProductDetails(self):
        print(f"Product Name: {self.product_name}\nProduct Number: {self.product_num}\nDescription: {self.product_description}\nPrice: {self.product_price} RS\n")
    


 
class SculptureTraining:
    def __init__(self,trainer_name,trainer_id,training_duration,training_level,training_price):
        self.trainer_name = trainer_name
        self.trainer_id = trainer_id
        self.training_duration = training_duration
        self.training_level = training_level
        self.training_price = training_price
    def getTrainingDetails(self):
        print(f"trainer Name: {self.trainer_name}\ntrainer id: {self.trainer_id}\nDuration: {self.training_duration} hours\ntraining Level: {self.training_level}\ntraining_Price: {self.training_price} RS\n")
    def bookingtrainingsession(self):
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        session_date = input("Enter the date for your training session (YYYY-MM-DD): ")

        # Store this information in a list or database for future reference
        session_data = [name, email, phone, address, session_date, self.trainer_name, self.training_duration]
        print("Training session booked successfully!")
        print(session_data)
class SculptureCompetition:
    def __init__(self,competition_name,competition_id,competition_description,rules,prize):
        self.competition_name = competition_name
        self.competition_id = competition_id
        self.competition_description = competition_description
        self. rules= rules
        self.prize = prize
    def getCompetitionDetails(self):
        print(f"competition Name: {self.competition_name}\ncompetition id: {self.competition_id}\ncompetition_description: {self.competition_description}\nrules: {self.rules}\nprize: {self.prize}\n")
    

class SculptureWebsite:
    def __init__(self):
        pass

courses = []
for x in range(3):
    course_name = input("Enter the course name: ")
    course_description = input("Enter the course description: ")
    duration = input("Enter the duration (in hours): ")
    level = input("Enter the level: ")
    price = int(input("Enter the price (in RS): "))
    courses.append(SculptureCourse(course_name, course_description, duration, level, price))

# Print course details using getCourseDetails() method
for course in courses:
    course.getCourseDetails()
for course in courses:
    course.registeringcourse()
products = []
for y in range(3):
    product_name = input("Enter the product name: ")
    product_num = input("Enter the product number: ")
    product_description = input("Enter the product description: ")
    product_price = int(input("Enter the price (in RS): "))
    products.append(SculptureProduct(product_name,product_num, product_description, product_price))
for product in products:
    product.getProductDetails()


Trainings = []
for z in range(3):
    trainer_name = input("Enter the trainer name: ")
    trainer_id = input("Enter the trainer id: ")
    training_duration = input("Enter the duration (in hours): ")
    training_level = input("Enter the level: ")
    training_price = int(input("Enter the price (in RS): "))
    Trainings.append(SculptureTraining(trainer_name, trainer_id, training_duration, training_level,training_price))    
for Training in Trainings:
    Training.getTrainingDetails()
for Training in Trainings:
    Training.bookingtrainingsession()


Competitions = []
for z in range(3):
    competition_name = input("Enter the competition name: ")
    competition_id = input("Enter the competition id: ")
    competition_description = input("Enter the competition_description: ")
    rules = input("Enter the rules: ")
    prize = input("Enter the prize : ")
    Competitions.append(SculptureCompetition(competition_name, competition_id, competition_description,rules,prize))    
for Competition in Competitions:
    Competition.getCompetitionDetails()
