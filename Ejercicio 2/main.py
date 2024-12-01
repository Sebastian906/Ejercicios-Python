from datetime import datetime

def replaceText(text):
    filters = [["[COMPANY_NAME]", "Company Name"],
                ["[EMPLOYEE_NAME]", "Employee Name"],
                ["[CITY]", "City"],
                ["[COUNTRY]", "Country"],
                ["[PRICE]", "Price"]
            ]
    for filter in filters:
        print("What is the " + filter[1] + "?")
        textInput = input()
        text = text.replace(filter[0], textInput)
    
    return text.replace("[CURRENT_DATE]", datetime.today().strftime('%Y-%m-%d'))

contractFile = open("contract.txt", "r")
result = ""

for row in contractFile: 
    result += row
result = replaceText(result)

with open("contract_processed.txt", "w") as textFile:
    textFile.write(result)

