"""Route declaration."""
from flask import current_app as app
from flask import render_template, request
import io, sys

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

nav = [
    {"name": "Início", "url": ""},
]

def highlightCode(code: str):
    formatter = HtmlFormatter(full=True, style='monokai', linenos=True)
    return highlight(code, PythonLexer(), formatter=formatter)

@app.route("/")
def home():
    """Landing page route."""
    return render_template(
        "home.html",
        nav=nav,
        title="ExecPy",
        description="Rode o seu comando python.\nFaça um print(...) para ver resultados.",
    )

@app.route("/convert", methods=["POST"])
def convert():
    if request.method == "POST":
        data = list(request.form.values())[0]  
        return highlightCode(data)
    return None


@app.route("/exec", methods=["POST"])
def execute():
    if request.method == "POST":
        data = list(request.form.values())[0] 
        return getOutput(data)
    return None

def getOutput(mycode): 
    print(sys.version)

    #keep a named handle on the prior stdout 
    old_stdout = sys.stdout 
    #keep a named handle on io.StringIO() buffer 
    new_stdout = io.StringIO() 

    #Redirect python stdout into the builtin io.StringIO() buffer 
    sys.stdout = new_stdout 

    #variable contains python code referencing external memory
    try:
        exec(mycode)
    except Exception as e: 
        print(e)

    #stdout from mycode is read into a variable
    result = sys.stdout.getvalue().strip()

    #put stdout back to normal 
    sys.stdout = old_stdout 
    
    print("result of mycode is: '" + str(result) + "'") 
    return result