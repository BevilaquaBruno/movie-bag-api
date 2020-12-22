from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
  {
    "name": "The Shawshank Redemption",
    "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
    "genres": ["Drama"]
  },
  {
    "name": "The Godfather ",
    "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
    "genres": ["Crime", "Drama"]
  }
]

@app.route('/movies', methods=['GET'])
def all_movies():
  return jsonify({'err': False, 'data': movies})

@app.route('/movies', methods=['POST'])
def add_movie():
  movie = request.get_json()
  movies.append(movie)
  return jsonify({'err': False, 'data': { 'id': len(movies)}}), 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
  if (len(movies) -1) < index or index < 0:
      return jsonify({'message': 'This movie does not exists.', 'err': True}), 404
  movie = request.get_json()
  movies[index] = movie
  return jsonify({'err': False, 'data': movies[index]}), 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
  if (len(movies) -1) < index or index < 0:
      return jsonify({'message': 'This movie does not exists.', 'err': True}), 404
  movies.pop(index)
  return jsonify({'err': False, 'data': 'None'}), 200

app.run()