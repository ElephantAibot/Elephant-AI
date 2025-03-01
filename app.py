
3. **Create app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from models.text_generator import generate_sales_copy
from models.image_processor import generate_poster
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['POSTER_FOLDER'] = 'static/posters'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Text input processing
        if 'keywords' in request.form:
            keywords = request.form['keywords']
            copy_text = generate_sales_copy(keywords)
            return render_template('result.html', copy=copy_text)
        
        # Image upload processing
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                # Save uploaded image
                img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(img_path)
                
                # Generate copy and poster
                copy_text = generate_sales_copy(img_path, is_image=True)
                poster_path = generate_poster(img_path, copy_text)
                return render_template('result.html', copy=copy_text, poster=poster_path)
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['POSTER_FOLDER'], exist_ok=True)
    app.run(debug=True)
