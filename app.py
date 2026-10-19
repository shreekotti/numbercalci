from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    number_a = ""
    number_b = ""
    operation = "add"

    if request.method == "POST":
        number_a = request.form.get("number_a", "").strip()
        number_b = request.form.get("number_b", "").strip()
        operation = request.form.get("operation", "add")

        try:
            a = float(number_a)
            b = float(number_b)

            if operation == "subtract":
                if a < b:
                    error = "Number A must be greater than or equal to Number B for subtraction."
                else:
                    result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "add":
                result = a + b
            else:
                error = "Please choose Add, Subtract, or Multiply."
        except ValueError:
            error = "Please enter a valid number in both fields."

    return render_template(
        "index.html",
        number_a=number_a,
        number_b=number_b,
        operation=operation,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    # Local development only. A production web server is used in the container.
    app.run(debug=True)
