for backend:####################################################

go to D:\ExcelApp\SimpleApi\

open terminal
create virtual environment --> py -m venv .env

activate virtual environment by --> ./.env/scripts/activate

now install packages from requirements.txt  -->  pip install -r requirements.txt

run xampp

go to fileupload directory

run the following commands:
py manage.py makemigrations
py manage.py migrate

run the project by:
py manage.py runserver

if another port is required then
py manage.py runserver [port]

for frontend:##############################################

open terminal

change directory to Frontend

run >> 'npm install'

now run >> 'npm run dev'
