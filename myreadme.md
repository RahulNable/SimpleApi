for backend:####################################################

open terminal
create virtual environment --> py -m venv .env

activate virtual environment by --> .\.env\Scripts\activate

        if any error occurs like: 
        \.env\Scripts\Activate.ps1 cannot be loaded because running  
        scripts is disabled on this system. For more information, see about_Execution_Policies

        run >> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

now check your python version and accoring to that download .whl file from 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient'

to install run >> 'pip install <filename>'

now install packages from requirements.txt  -->  pip install -r requirements.txt

run xampp and create new database by name>> 'excel_database'

in terminal go to fileupload directory >>>  cd fileupload

run the following commands:
py manage.py makemigrations
py manage.py migrate

run the project by:
py manage.py runserver

if another port is required then
py manage.py runserver [port]

for frontend:##############################################

open new terminal

change directory to Frontend >> cd Frontend

run >> 'npm install'

now run >> 'npm run dev'
