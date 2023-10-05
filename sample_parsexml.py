import xml.etree.cElementTree as et 

tree = et.parse("sample.xml")
root = tree.getroot()

job_title = []
company_name = []
category = []
city = []

for title in root.iter('job_title'):
    job_title.append(title.text)

for company in root.iter('company_name'):
    company_name.append(company.text)

for gory in root.iter('category'):
    category.append(gory.text)

for ci in root.iter('city'):
    city.append(ci.text)

print("Job Title", job_title)
print("Company Name", company_name)
print("Categroy", category)
print("City", city)