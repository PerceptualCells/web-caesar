from flask import Flask, request
from caesar import rotate_string

 
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!doctype html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px;
                width: 520px;
                height: 120px;
            }}
        </style>        
    </head>            
    <body>
         <form action="/add" method="post">
         <label>
            Rotate by:
            </label>
            <input type="text" name="rot" value="0"/>
            <textarea type="text" name="plaintext">{0}</textarea>
         
        <input type="submit" value="encrypt"/>
    </form>
     </body>
</html>
"""


@app.route("/")
def index():
    
    return form.format("")

@app.route("/add", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["plaintext"]
    rot = int(rot)

    q = rotate_string(text, rot)
    return form.format(q)


app.run()
