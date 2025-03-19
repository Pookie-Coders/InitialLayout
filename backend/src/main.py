# go to cmd : paste the below
# curl -X POST http://127.0.0.1:5000/recommend -H "Content-Type: application/json" -d "{\"liked_movie\": \"Avengers: Endgame\"}"

from flask import Flask, request, jsonify
from recommendation import get_recommendations

app = Flask(__name__)

@app.route("/recommend", methods=["POST"])
def recommend():
    """API endpoint to get movie recommendations based on user input."""
    data = request.json  # Get JSON data from frontend
    liked_movie = data.get("liked_movie")

    if not liked_movie:
        return jsonify({"error": "Please provide a movie name"}), 400

    recommendations = get_recommendations(liked_movie)

    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
