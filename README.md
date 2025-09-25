# Kicks Project

A website for selling shoe products.

Built with **Python**, **Django**, **Django REST Framework**, **REST JWT**, and more.

---

## Note

This app is designed **only to provide APIs** and is **not a fully developed frontend website**.  
It is meant to be completed when the frontend stack is implemented.

---

## Installation

1. Create a directory on your desktop:

```bash
mkdir kicks
cd kicks
Initialize git and clone the repository:

bash
Copy code
git init
git clone https://github.com/1ArsalanAmiri/kicks
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Run the development server:

bash
Copy code
python manage.py runserver 8000
Accessible APIs
app: accounts
POST /api/accounts/register
Register a new user.

POST /api/accounts/request-otp
Request a one-time password (OTP) for verifying the user via email.
Note: For development mode, the OTP is set to 123456.

POST /api/accounts/verify-otp
Verify the entered OTP code and create the user in the database.
Also returns the access and refresh tokens for authentication purposes.

app: products
GET /api/products
Returns a JSON list of submitted products in the database.

GET /api/products/<slug>
Returns the details of a specific product.

GET /api/products/slug/<slug>/similar
Returns similar products to the base product within the same category.

POST /api/products/filter
Filter products based on specific criteria.
