from flask import Flask, request, jsonify
import os

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

import video_split as vs
import text_generate as tg
import store_captions as sc

@app.route("/upload-video", methods=["POST"])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    query = request.form.get('query', '')  # Retrieve query from the request

    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(video_path)
        output_folder = "output_frames"
        num_frames = 80
        vs.split_video_into_frames(video_path, output_folder, num_frames)
        captions = tg.generate(output_folder, query)  # Pass the query to the generate function
        sc.add_captions_to_json(file.filename, captions)
        
        return jsonify({'message': 'Video uploaded and processed successfully'})

if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = 'uploads'
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
