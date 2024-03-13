from flask import Flask, render_template, request, send_file, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

desktop_path = os.path.expanduser("~/Desktop")
data_folder = os.path.join(desktop_path, "MyData")
file_path = os.path.join(data_folder, "datasav.txt")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    quantity = request.form.get('quantity')
    weight = request.form.get('weight')
    number = request.form.get('number')

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    with open(file_path, 'w') as file:
        file.write(
            f'Дата: {current_time}, Количество: {quantity}, Вес: {weight}, Номер: {number}\n')

    # Перенаправление на маршрут /download
    return redirect(url_for('download'))


@app.route('/download')
def download():
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
