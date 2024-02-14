import React, { useState } from 'react';
import '../styles/uploadPageStyles.css'; // Import the CSS file

const UploadPage = () => {
    const [file, setFile] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [message, setMessage] = useState("");
    const [query, setQuery] = useState(""); // State to store the query
    const [videoKey, setVideoKey] = useState(0); // Unique key for the video element

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setMessage(""); // Reset message when a new file is selected
        setVideoKey(prevKey => prevKey + 1); // Update the key to force re-render of video element
    };

    const handleQueryChange = (e) => {
        setQuery(e.target.value);
    };

    const handleUpload = () => {
        if (!file) return;
        setUploading(true);
        const formData = new FormData();
        formData.append('file', file);
        if (query.trim() !== "") { // Include query only if not empty
            formData.append('query', query);
        }
        fetch("/upload-video", {
            method: 'POST',
            body: formData
        }).then(
            res => res.json()
        ).then(
            data => { 
                setMessage(data.message);
                setUploading(false);
            }
        ).catch(error => {
            console.error('Error:', error);
            setUploading(false);
        });
    };

    return (
        <div className="upload-container">
            <div>
                <input type="file" accept="video/*" onChange={handleFileChange} />
                <input type="text" placeholder="Enter query" onChange={handleQueryChange} />
                <button onClick={handleUpload}>Upload Video</button>
            </div>
            {uploading && <p className="loading">Generating...</p>}
            {message && <p className={`message ${message.startsWith("Error") ? 'error' : 'success'}`}>{message}</p>}
            {file && (
                <div>
                    <p>Uploaded Video:</p>
                    <video key={videoKey} controls>
                        <source src={URL.createObjectURL(file)} type="video/mp4" />
                        Your browser does not support the video tag.
                    </video>
                </div>
            )}
        </div>
    );
}

export default UploadPage;
