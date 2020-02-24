from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from bson.json_util import dumps
import re
from config import dbURL

client = MongoClient(dbURL)
print(f"Connecting to {dbURL}")


@jsonErrorHandler
def getCompanyWithName(name):
    companies = client.get_default_database()["cleancompanies"]
    namereg = re.compile(name, re.IGNORECASE)
    print(namereg)
    query = companies.find_one({"name": namereg})
    if not query:
        raise ValueError("Company not found")
    return dumps(query)
