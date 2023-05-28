from flask import Flask, request, abort, Response

from solution import Solution

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def check_parenthesis_generation():
    if request.method == 'POST':
        solver = Solution()
        n = int(request.form['number'])
        try:
            result = solver.generateParenthesis(n)
        except ValueError:
            abort(400)
        return ' '.join(str(x) for x in result)
    else:
        return f"<html><head><title>This is Test App Title</title></head>" \
               f"<body><h1>This is Test App Header</h1>" \
               f'<form action="/result" method="POST">' \
               f'<input type="number" name="number" id="number">' \
               f'<input type="submit" value="Submit" id="submit">' \
               f'</form></body></html>'


@app.route("/result", methods=['POST'])
def check_parenthesis_generation_result():
    if request.method == 'POST':
        solver = Solution()
        n = int(request.form['number'])
        try:
            result = solver.generateParenthesis(n)
        except ValueError:
            abort(400)
        result_string = ' '.join(str(x) for x in result)
        res = f"<html><head><title>This is Test App Title</title></head>" \
              f"<body><h1>This is Test App Header</h1>" \
              f'<form action="/result" method="POST">' \
              f'<input type="number" name="number" id="number" value={n}>' \
              f'<input type="submit" value="Submit" id="submit">' \
              f'<div id="result">{result_string}</div>' \
              f'</form></body></html>'
        response = Response(res)
        return response
