from flask import Flask, jsonify

app = Flask(__name__)

# Define the available subjects, levels, and lessons
subjects = ['arabic', 'english', 'math']
levels = ['level1', 'level2', 'level3']
lessons = {
    'arabic': {
        'level1': {
            'lesson1': 'Arabic lesson 1 data',
            'lesson2': 'Arabic lesson 2 data'
        },
        'level2': {
            'lesson1': 'Arabic lesson 3 data',
            'lesson2': 'Arabic lesson 4 data'
        },
        'level3': {
            'lesson1': 'Arabic lesson 5 data',
            'lesson2': 'Arabic lesson 6 data'
        }
    },
    'english': {
        'level1': {
            'lesson1': 'English lesson 1 data',
            'lesson2': 'English lesson 2 data'
        },
        'level2': {
            'lesson1': 'English lesson 3 data',
            'lesson2': 'English lesson 4 data'
        },
        'level3': {
            'lesson1': 'English lesson 5 data',
            'lesson2': 'English lesson 6 data'
        }
    },
    'math': {
        'level1': {
            'lesson1': 'Math lesson 1 data',
            'lesson2': 'Math lesson 2 data'
        },
        'level2': {
            'lesson1': 'Math lesson 3 data',
            'lesson2': 'Math lesson 4 data'
        },
        'level3': {
            'lesson1': 'Math lesson 5 data',
            'lesson2': 'Math lesson 6 data'
        }
    }
}

# Define the API endpoints
@app.route('/')
def index():
    return 'Welcome to the API!'

@app.route('/subjects')
def get_subjects():
    return jsonify(subjects)

@app.route('/levels')
def get_levels():
    return jsonify(levels)

@app.route('/lessons/<string:subject>/<string:level>')
def get_lessons(subject, level):
    # Check if the subject and level are valid
    if subject not in subjects:
        return jsonify({'error': 'Invalid subject'}), 400
    if level not in levels:
        return jsonify({'error': 'Invalid level'}), 400

    # Return the list of lessons for the subject and level
    return jsonify(lessons[subject][level])

@app.route('/lesson/<string:subject>/<string:level>/<string:lesson>')
def get_lesson(subject, level, lesson):
    # Check if the subject, level, and lesson are valid
    if subject not in subjects:
        return jsonify({'error': 'Invalid subject'}), 400
    if level not in levels:
        return jsonify({'error': 'Invalid level'}), 400
    if lesson not in lessons[subject][level]:
        return jsonify({'error': 'Invalid lesson'}), 400

    # Return the text data for the lesson
    return jsonify({'text_data': lessons[subject][level][lesson]})

if __name__ == '__main__':
    app.run()
