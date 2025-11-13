from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    query = request.args.get('q')
    if query:
        items = conn.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + query + '%',)).fetchall()
    else:
        items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    conn = get_db_connection()
    conn.execute("INSERT INTO items (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        conn.execute("UPDATE items SET name = ? WHERE id = ?", (name, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    item = conn.execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template('form.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
    conn.close()
    app.run(debug=True)
