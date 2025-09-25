Kicks Project

A webstie for selling shoes products.

made with Python , Django , Django REST Framework , REST JWT , and ...

NOTE : This app is only made for returning API's and its not a kind of full developed website .
and it meant to be compelete if the front-end stack is done .


INSTALLATION :
first make a directory in your desktop :

CMD :
    mkdir kicks
    cd kicks 
    git init 
    git clone https://github.com/1ArsalanAmiri/kicks

when cloning is is done : 
    pip install -r requirements.txt 

when downloading packages is done :
    python.exe manage.py runserver:8000

accessable API's:
    app:accounts
    localhost:8000/api/accounts/register  "registering a user"
    localhost:8000/api/accounts/request-otp  "requesting a one time password for verifying the user via email Verification NOTE: the set otp for developing mode is 123456"
    localhost:8000/api/accounts/verify-otp   "verifying the entered otp code and creating user in database , also: returning the access and refresh code to the front-end developer for using authenticational purposes"
    app:products
    localhost:8000/api/products  "returns a JSON list of submited products in database"
    localhost:8000/api/products/"slug" "returns the product details"
    localhost:8000/api/products/slug/"similar"  "returns the similar products to the base product with the same category"
    localhost:8000/api/products/filter  "filtering the products with some specefic details"
    


    
