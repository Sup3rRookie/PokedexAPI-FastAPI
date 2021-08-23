'''
API Design:
- Customer:
    1. Create new customer
    2. Get customer by ID
    3. Create invoce for customer
    4. Get all invoices for customer

- Invoice:
    1. Get specific invoice details (plus stock codes)
    2. Invoce add stock code

- Stock Code:
    1. Get specific stock code details
'''

# import relavant modules
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional

# This help to turn classes into JSONs and return JSONs Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# creating API structure
class Customer(BaseModel):
    customer_id: str
    country: str
    city: Optional[str] = None

class URLLink(BaseModel):
    url: str

class Invoice(BaseModel):
    invoice_no: int
    invoice_date: str
    customer: Optional[URLLink] = None

fakeInvoiceTable = dict()

# General Execuion and to dockerize the app
app = FastAPI()

# Base URL
@app.get('/')
async def root():
    return {'message':'Creating APIs using FastAPI'}


# Add a new Customer
@app.post('/customer')
async def create_customer(item: Customer): #Body awaits a json with customer info
    # This is how to work with and return an item
        # country = item.country
        # return {item.country}

    # Add here for creating a customer and save it in the DB

    # Encode the created customer item if successful into a JSON and return it to the response
        print()