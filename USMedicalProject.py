import csv

# Our main variables for analyisis:

age = []
sex = []
bmi = []
num_of_children = []
smoker_status = []
region = []
charges = []

def extract_csv(lst, column_name):
    with open(r'c://Users//tyler//OneDrive//Documents//Tech//Coding Projects//US Medical Project//insurance.csv') as medical_insurance_data:
        csv_dict = csv.DictReader(medical_insurance_data)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

# Here I plugged in the variables from above

extract_csv(age, 'age')
extract_csv(sex, 'sex')
extract_csv(bmi, 'bmi')
extract_csv(num_of_children, 'children')
extract_csv(smoker_status, 'smoker')
extract_csv(region, 'region')
extract_csv(charges, 'charges')

# As the variables extracted from the CSV file are read as string/text in Python I use the below functions to convert them into their respective integer and float values

int_num_of_children = []
for child in num_of_children: 
    int_num_of_children.append(int(child))

float_bmi = []
for stat in bmi:
    float_bmi.append(float(stat))

int_age = []
for stat in age: 
    int_age.append(int(stat))

float_charges = []
for cost in charges: 
    float_charges.append(float(cost))

# Statistics about the data such as mean, minimum and maximum values, etc. 

def general_stats(int_age): 
    num_of_clients = len(age)
    general_statement = "There are {num_of_clients} participants in this study.".format(num_of_clients=num_of_clients)
    return general_statement 

general_info = general_stats(int_age)
print(general_info)

def other_stats(int_age, float_bmi, int_num_of_children, float_charges):
    min_age = min(int_age) 
    max_age = max(int_age)
    min_bmi = min(float_bmi)
    max_bmi = max(float_bmi)
    min_num_of_children = min(int_num_of_children)
    max_num_of_children = max(int_num_of_children)
    min_cost = round(min(float_charges), 2)
    max_cost = round(max(float_charges), 2)
    other_statement = "The lowest age for our clients is reported to be {min_age} years old while our highest is {max_age} years old. The lowest bmi reported is {min_bmi} while our highest is {max_bmi}. The smallest number of children reported is {min_num_of_children} children while the highest is {max_num_of_children}. The lowest cost charged among clients is ${min_cost} while the highest is ${max_cost}.".format(min_age=min_age, max_age=max_age, min_bmi=min_bmi, max_bmi=max_bmi, min_num_of_children=min_num_of_children, max_num_of_children=max_num_of_children, min_cost=min_cost, max_cost=max_cost) 
    return other_statement

other_info = other_stats(int_age, float_bmi, int_num_of_children, float_charges)
print(other_info)

def average_stats(int_age, sex, float_bmi, num_of_children, float_charges):
    average_age = round(sum(int_age)/len(int_age), 2)
    average_bmi = round(sum(float_bmi)/len(float_bmi), 2)
    average_num_of_children = round(sum(int_num_of_children)/len(int_num_of_children), 2)
    average_cost = round(sum(float_charges)/len(float_charges), 2)
    average_statement = "The average age of health insurance clients was {average_age} years old. The average BMI was {average_bmi}. The average number of children that a client had was {average_num_of_children} children. The average cost of health insurance was ${average_cost}.".format(average_age = average_age, average_bmi = average_bmi, average_num_of_children = average_num_of_children, average_cost = average_cost)
    return average_statement 

average_info = average_stats(int_age, sex, float_bmi, num_of_children, float_charges)
print(average_info)

def mode(region, smoker_status, sex): 
    mode_region = max(region.count("southwest"), region.count("southeast"), region.count("northeast"), region.count("northwest"))
    if mode_region == region.count("southwest"):
        top_us_region = "southwestern"
    elif mode_region == region.count("southeast"): 
        top_us_region = "southeastern"
    elif mode_region == region.count("northeast"): 
        top_us_region = "northeastern"
    elif mode_region == region.count("northwest"):
        top_us_region = "northwestern"
    if smoker_status.count("yes") > smoker_status.count("no"): 
        mode_smoker_status = "do"
    else: 
        mode_smoker_status = "don't"
    mode_smoker_count = max(smoker_status.count("yes"), smoker_status.count("no"))
    if sex.count("male") > sex.count("female"): 
        mode_sex = "men"
    else: 
        mode_sex = "women"
    mode_sex_count = max(sex.count("male"), sex.count("female"))
    mode_statement = "The {top_us_region} region of the United States represented the region with the most clients in the United States ({mode_region} clients). More clients overall have stated that they {mode_smoker_status} smoke with {mode_smoker_count} clients reporting. As far as sex, we find that more participants are {mode_sex} in the dataset with {mode_sex_count} clients reporting as such.".format(top_us_region=top_us_region, mode_region=mode_region, mode_smoker_status=mode_smoker_status, mode_smoker_count=mode_smoker_count, mode_sex=mode_sex, mode_sex_count=mode_sex_count)
    return mode_statement

mode_info = mode(region, smoker_status, sex)
print(mode_info)

# In-depth statistics variable by variable
def cross_sect_stats(int_age, sex, float_bmi, int_num_of_children, smoker_status, region, float_charges):
    pass



# This creates a dictionary of each entry in the CSV file.

def dataset_dict(int_age, sex, float_bmi, int_num_of_children, smoker_status, region, float_charges): 
    dict_categories = ["Age", "Sex", "BMI", "Number of Children", "Smoker Status", "Region", "Cost"]
    medical_data = list(zip(int_age, sex, float_bmi, int_num_of_children, smoker_status, region, float_charges))
    for stat in medical_data: 
        medical_combo = list(zip(dict_categories, stat))
        medical_dict = dict(medical_combo)
        print(medical_dict)
 
        

medical_dictionary = dataset_dict(int_age, sex, float_bmi, int_num_of_children, smoker_status, region, float_charges)
print(medical_dictionary)

# This creates a dictionary of a user's medical information. 

class MedicalHistory: 
    def __init__(self, name, age, sex, bmi, num_of_children, smoker_status, region, charges):
        self.name = name 
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker_status = smoker_status
        self.region = region
        self.charges = charges
    
    def dict(self): 
        medical_dict = {"Name": self.name, "Age": self.age, "BMI": self.bmi, "Number of Children": self.num_of_children, "Smoker Status": self.smoker_status, "Region": self.region, "Cost": self.charges}
        return medical_dict