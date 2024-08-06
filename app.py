import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = 'AIzaSyCSlgUDH8WiibVCr92qMWxc-MmJw24RP8M'  
SEARCH_ENGINE_ID = 'f196234257b7f4d2f'  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    # Extract the search term from the URL parameters
    query = request.args.get('query')
    if query:
      
        url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}'
        # Make the API request and get the response
        response = requests.get(url)
        # Convert the response to JSON
        data = response.json()
        # Extract the search results from the JSON response
        results = data.get('items', [])
    else:
        results = []
    # Render the results.html template with the search results
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)  