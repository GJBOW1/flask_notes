# Flask Notes - Coding Dojo 2023 - Gregg Bowen

# In this chapter, we will use a micro-framework called Flask to teach you the main components of web applications. Here are the concepts we'll focus on in this chapter:

# Rendering Templates
# Redirecting
# Form data
# GET & POST requests
# Session

# *Flask Flow

# In the image flask_flow, we can see how a basic flask application works.

# *Flow:

# 1. The HTTP request is made and hits the server.py file.
# 2. Based on the route we give, it gathers up any HTML, CSS, JS, and data.
# 3. Then it responses back to the browser with what we return.

# *Virtual Environments:

# When we are working as a developer, we might find ourselves working on different projects or teams in our work 
# place. These projects might use the same programming language, but different versions and packages along the 
# way. How do we keep ourselves organized and avoid conflicts with our OS? With Python the answer is Virtual 
# Environments.

# *Installing our Virtual Environment tool
# While there are a couple different ways to create virtual environments, we are going to be using pipenv to 
# streamline the process. To get started we need to use pip to install pipenv globally.

# Windows:
# pip install pipenv

# Mac:
# pip3 install pipenv


# *Creating our Virtual Environment and Installing Flask
# Now that we have pipenv installed, let's create a new project folder. Using the folder structure we created on 
# day one, create a new folder inside the python_/flask/fundamentals folder called hello_flask.

# Navigate into the hello_flask folder using your terminal or command prompt. Once we are in the project folder 
# we can use pipenv to install Flask.

# pipenv install flask


# The first time we run pipenv install, it will create 2 files for us, Pipfile and Pipfile.lock. Both are needed 
# in order to use the installed packages, but difference between the two include: Pipfile will display the 
# packages installed, and Pipfile.lock will have the specific details on what version is being used.

# ***NOTE*** If your receive an error using pipenv, you may need to import it as a module first before it can 
# be run as a script. You can do so using the -m flag as below. You will need to do this every time you use pipenv.

# Windows:
# python -m pipenv <command to use>

# Mac:
# python3 -m pipenv <command to use>

# *Activating our Virtual Environment
# Once we have installed the Flask package, we need to activate our environment in order to use it. We can 
# achieve this with the following command.

# pipenv shell

# Notice the additional folder with the parentheses, (hello_flask), this is showing us the environment is active.

# *Checking What's Installed with pip list
# To check what is installed in your virtual environment, with your virtual environment activated (pipenv shell), 
# you can type the command, pip list and you will see a list of what is currently installed. For instance if 
# you wanted to verify for a particular project that you have Flask installed you would activate your 
# environment then use this command as shown below.

# pip list

# *Deactivating our Virtual Environment
# To deactivate the virtual environment we can use exit. Our bash window should look something like this.

# exit

# *IMPORTANT DISCLAIMER
# Do not create a virtual environment within another virtual environment.

# Helpful Links:
# Pipenv: https://pipenv.pypa.io/en/latest/

# *Building the Application
# Let's start by building a basic "hello world" app in Flask:

# 1. Inside the "hello_flask" folder, create a file called server.py
#     This will be our "server" file where we will set up all of our routes to handle requests.
#     You'll want to create a new folder for each assignment moving forward. It will seem tedious at first, but 
#     as we add additional files to each project, we'll want to keep everything organized by assignment/project!
# 2. Next, put the following code inside of server.py:

# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.

# Notice how we are accessing the app object and running the route method, passing in a string that is the route 
# that we want to add to our application. You must do this for every route that you want to add to our application.

# Note: Moving forward, you may see some red squiggly lines under your import statements because your text 
# editor's linter doesn't recognize packages in your virtual environment. You can ignore them unless running 
# the file actually gives you errors!

# Now start the application! Navigate to your project directory and run the server.py file as shown below.
# Note: the command you need to type from the example below is what comes after the $. Your terminal prompt 
# may look slightly different, but seeing (hello_flask) part of the terminal prompt is a sign that your virtual 
# environment is active. Be sure it is before you run the file!

# Windows:
# (hello_flask) hello_flask $ python server.py

# Mac: 
# (hello_flask) hello_flask $ python3 server.py

# Now if you navigate to localhost:5000/ in your browser, you should see the message "Hello World!"

# *What did you just do?
# You just created your first web server!

# Why are we going to localhost:5000? The Flask web server you created listens for an HTTP request on port 5000 
# (notice in your terminal that your code is constantly running). Whenever a request is sent to localhost:5000, 
# the server looks at the URL being requested and sends the appropriate response. If we go to route "/", the 
# hello_world() function will run. Since we (or the client) called the function, we receive what the function 
# returns!

# We also did a couple of important things in the code above:

# 1. We imported the Flask class. You will need this line in every application you build with Flask.
# 2. We made an instance of the Flask class called "app". You will need this line in every application you build 
# with Flask.
# 3. We set up a routing rule using the "@" decorator with the route method: @app.route("/route_string"). The routing 
# rule is associated with the function immediately following it.
# 4. Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.

# *Changing the Port
# Some students may find that port 5000 is already in use. If you've used it for running a flask project already 
# with no issues, likely you just have a terminal already open running a project. However, if you find the port 
# is being used by your machine for another purpose, common for some versions of macOS, changing the port just 
# requires adding some arguments to the app.run() function call. Port 8000 is a good alternative.

# app.run(debug=True, host="localhost", port=8000)

# *Routes:
# Routes are an essential part of any web application. A route is much like a variable name we assign to a request. The job of a route is to communicate to the server what kind of information the client needs. This route name is attached to a route on our server that points towards a specific set of instructions. These instructions contain information about how to interpret the data being sent, the operations that need to be completed, and the response that should be sent back. These instructions are the code we'll be creating!

# Every route has two parts:

# 1. HTTP method (GET, POST, PUT, PATCH, DELETE)
# 2. URL

# *Setting up your Routes
# Let's add another route to our server.py file:

# # import statements, maybe some other routes
    
# @app.route('/success')
# def success():
#   return "success"
    
#     # app.run(debug=True) should be the very last statement! 

# Now we have 2 routes--if the client requests localhost:5000/, the hello_world function will run. But if the client requests localhost:5000/success, the success function will run.

# What if we wanted to be able to say "Hello, Michael" or "Hello, Amy" or "Hello, Wes"? We could make three 
# routes, but that feels pretty repetitive. Also, every time we want to include someone else, we would need 
# to create a new route. This is a great opportunity to add variable rules to our routes. For the example 
# above, we could make the name a variable, like so:

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name

# We can add as many of these as we need, giving each variable a different name:

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

# The localhost:5000 part of the route determines which server to call upon. The rest of the route, including the "/", tells the server which function should be invoked.

# *Type Converters
# Another feature of variable rules is the ability to designate an expected type for a route variable. For this 
# you can use what Flask calls 'converters.' By default a route variable is passed as a string, even if the 
# character(s) are numbers. In the example below we designate int as the converter, which indicates that we are 
# expecting an integer to be passed through in that part of the route string. Flask will then cast the argument 
# into the type specified, converting for example, the string '8' into the integer 8.

# # Here the second parameter is cast into an integer before being passed to the function
# @app.route('/hello/<name>/<int:num>') 
# def hello(name, num):
#     return f"Hello, {name * num}"

# In python when you multiple a string by an integer, let's say num, it will just make a longer string with the original 
# string repeated num number of times, whereas if you multiply a string by another string, it will throw an error.

# For the example above, if you navigate to "localhost:5000/hello/Adrien/3" you would see the following in your browser.

# Something to note, is that if I were to navigate to "localhost:5000/hello/Adrien/notANumber" Flask would return a 
# '404 not found' error to the client, since the string 'notANumber' cannot be converted to an integer.

# The take home is that you can use converters on route variables to specify and enforce data types other than strings.

# *Your First Web Application!
# Although the code we show above is brief, we're bringing together a lot of concepts you've never seen before. 
# Test out all the code snippets we've given you to this point to make sure you understand how everything's 
# working. While it doesn't do much, you've created your first web application! The next assignment will help 
# you practice these concepts. If you're having trouble piecing everything together, watch the video above to 
# see all this code in action.

# *Rendering Views:

# In the last assignment, we just returned simple strings. But we spent all that time in Web Fundamentals 
# learning HTML--isn't that really what we want to return? You bet. We just need a place to save them so that 
# our Flask server file knows where to find them. In Flask, we must create a directory alongside our server.py 
# file called templates (exactly this word, plural). Inside the templates directory, we'll add our HTML files. 
# Going back to our hello_flask project:

# FILE: /hello_flask/templates/index.html

# <h1>Hello Flask!</h1>  

# Then in our code, we refer to our HTML files like so:

# FILE: /hello_flask/server.py

# from flask import Flask, render_template  # added render_template!
# app = Flask(__name__)                     
    
# @app.route('/')                           
# def hello_world():
#     # Instead of returning a string, 
#     # we'll return the result of the render_template method, passing in the name of our HTML file
#     return render_template('index.html')  
    
# if __name__=="__main__":
#     app.run(debug=True)                   

# note the addition of render_template -- that allows us to return the rendered HTML that we created above. 
# Now when we run our server.py file and go to localhost:5000/, we'll see our template!

# Here you can see that we are handling the root route, or '/', route with the hello_world function which 
# renders the index.html template. Here the HTTP verb is "GET".

# *Template Engines:

# While sometimes we'll want to render static HTML, we'll often want to pass data to allow for dynamic content 
# on a given HTML file. This is where template engines are useful. Since our browser doesn't understand Python 
# code, the render_template function sends our HTML file--along with any data passed--through the template 
# engine to resolve any code into HTML. The final product is the response to the client.

# *Passing Data to the HTML
# Let's see this in action by building off of our hello_flask project directory. Notice that in our 
# render_template function call, we are now passing three arguments! The first one is still the name of the 
# HTML file, but the other two have names and values:

# FILE: hello_flask/server.py

# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
# if __name__=="__main__":
#     app.run(debug=True)

# *Rendering Data on a Template
# Now how do we use that data on the HTML? There are 2 special inputs we can use to insert Python-like code into our Flask templates.

# {{ some variable }}
# {% some expression %}

# Let's update our index.html file:

# FILE: hello_flask/templates/index.html

# <h3>My Flask Template</h3>
# <p>Phrase: {{ phrase }}</p>
# <p>Times: {{ times }}</p>
      
# {% for x in range(0,times): %}
#     <p>{{ phrase }}</p>
# {% endfor %}
      
# {% if phrase == "hello" %}
#   <p>The phrase says hello</p>
# {% endif %}

# In the above code, we used the different embedding tags to output some of our variables, insert a for-loop, 
# and do some conditional checking with an if statement in our HTML template. It's especially important to see 
# how we used the values that we passed into our template from our server file in the embedding tags.

# These tags allow us to control what gets rendered (if statements), how many times something gets rendered 
# (for loop) and printing values to our rendered html.

# Although you technically can do a lot of logic in your templates, you should try to limit that logic as much 
# as possible. Do the bulk of your logic in your Python code. If you put too much logic in your templates, you 
# may slow down your server response time.

# As we mentioned previously, Flask uses a templating engine called Jinja. Jinja has a lot of great built-in 
# features that allow us to place dynamic information on HTML pages. Check out the Jinja documentation here:
# https://login.codingdojo.com/m/517/12986/91160#:~:text=Jinja%20documentation%20here%3A-,Jinja%20Template%20Docs,-IMPORTANT%20NOTE%3A%20Using

# IMPORTANT NOTE: Using HTML comments (<!-- -->) will NOT comment out Jinja. You must use Jinja commenting syntax instead.
# Which you can find here: https://login.codingdojo.com/m/517/12986/91160#:~:text=Jinja%20commenting%20syntax

