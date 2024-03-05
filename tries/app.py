from flask import Flask, request, jsonify,render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_pages():
    folder_id = "10clN-KH-3B9lg4W3ProYKKoFjtpjDF61"
    from fetch_all_page_token_With_dates import get_pages_from_drive
    pages = get_pages_from_drive(folder_id)
    return render_template("index.html",pages=pages)


if __name__ == "__main__":
    app.run(debug=True)