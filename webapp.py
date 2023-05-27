from flask import Flask, request, abort
from solution import Solution
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def generateParenthesis():
    if request.method == 'POST':
        solver = Solution()
        n = int(request.form['number'])
        try:
            result = solver.generateParenthesis(n)
        except ValueError:
            abort(400)
        return ' '.join(str(x) for x in result)
    else:
        return f"<html><body><h1>This is Test App</h1>" \
               f'<form action="/" method="POST">' \
               f'<input type="number" name="number">' \
               f'<input type="submit" value="Submit">' \
               f'</form></body></html>'
