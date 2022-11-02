<img src="https://user-images.githubusercontent.com/78557330/170858525-6e89b393-7e02-4615-9a88-7d9b2c0fa94e.png">

# Attendance Portal
This a an attendance tracker system which uses facial recognition technology for the same purpose.

## Tech Stack:
- **Flask** - A python framework for web development.
- **face_recognition** - library by Adam Geitgey
- **React** JavaScript Library for building user interfaces
- **Firebase** - For teachers authentication.
- **Bootstrap** - Building responsive designs.

## Features:

- ### Teacher
    - Teacher need to signup/signin to acces these features.
    - Can add new student using student name and admission no.
    - Can add test image (without it student will not be able to mark attendance)
    - Remove student from list.
    - Check the present/absent status of student and also date and time.
- ### Student
    - Can mark attendance by capturing his image from webcam and filling admission no. in form.
    - Along with all this, required response will be give if the face is **not detected** , **not matched** , or **already have been marked attended.**

## Local Setup
1. Clone the github repository.
```
https://github.com/sakshamp78/attendance-tracker.git 
```
2. Open the folder in Visual Studio Code.

3. There are two folders named as **client** and **server**.
- Go to the client directory :
```
cd client
```
4. Ensure that you have [Node.js](https://nodejs.org/en/) installed.
5. Install required dependencies by :
```
npm install
```
6. Start development server for react by running following command , this will start your application in http://localhost:3000/ :
```
npm start
```
**Since API is not hosted , we have to serve this as well as locally.**
**Our server is made on flask ,so ensure that [python](https://www.python.org/downloads/) is installed in your PC**
1. Open new terminal and go to the **server** directory by:
```
cd server
```
2. Create virtual environment by that will create an **env** file , install Virual-Environment if you don't have after this run :
```
virtualenv env
```
3. Now activate the virtual environment by :
```
.\env\Scripts\activate
```
By default in windows the execution property is set Restricted. This will restrict the activation of virtual environment. To change the execution policy use following commands on  Windows PowerShell as Administrator :
```
Set-ExecutionPolicy Unrestricted -Force
```
4. Now install the packages in requirements.txt file by :
```
pip install requirements.txt
```
OR
```
pip install -r requirements.txt
```
It is to be noted that **face_recognition** requires **dlib library** , and dlib requires C program to use.
Thus, install **VS Code community version** and install **Desktop development with C++** to install dlib. Detail of this is given [here](https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f#:~:text=Now%20we%20can%20install%20dlib,need%20to%20install%20CMake%20library.&text=Then%2C%20you%20can%20install%20dlib%20library%20using%20pip%20install%20.&text=After%20passing%20enter%2C%20you%20laptop,run%20the%20C%2C%20C%2B%2B%20Compiler.).

5. Now create a new database file by opening new terminal and running following commands :
```
python
```
```
from app import db
```
```
db.create_all()
```
After doing this you must be seeing a new .db file created in the backend directory.

6. Now open new terminal and confirm if virtual environment is activated or not , then run the development server for our API by :
```
python app.py
```
Now your API will be hosted on http://127.0.0.1:5000 .

**After following all the above instruction you can explore the Attendance Tracker application in your local server**
<p float="left">

</p>

