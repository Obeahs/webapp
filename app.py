from flask import Flask, render_template, request
import statistics

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', results=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    numbers = request.form['numbers']
    num_list = [float(num) for num in numbers.split(',') if num.strip()]
    
    max_value = max(num_list)
    avg_value = statistics.mean(num_list)
    stddev_value = statistics.stdev(num_list)
    
    results = {
        'max': max_value,
        'avg': avg_value,
        'stddev': stddev_value
    }
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
