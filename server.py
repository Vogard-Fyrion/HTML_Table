from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# for x in range(0, len(users)):
#     print(x)
#     print(users[x])
#     for y in users[x]:
#         print(y)
#         print(users[x][y])

@app.route('/')
def index():
    return render_template("index.html", users = users)

if __name__ == "__main__":
    app.run(debug = True)

