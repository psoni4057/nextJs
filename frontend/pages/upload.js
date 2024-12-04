import { useState, useRef } from 'react';
import axios from 'axios';

//send the request from the client side

export default function Upload() {
  const [text, setText] = useState('');
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');
  const fileInputRef = useRef(null);
  const textInputRef = useRef(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile ? selectedFile : null);
    
    // Clear the text input field when a file is selected 
    if (textInputRef.current) {
      textInputRef.current.value = '';
      setText('');
    }
  };

  const handleFileRemove = () => {
    setFile(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = ''; // Clear the file input element value
    }
  };

  const handleTextChange = (e) => {
    setText(e.target.value);

    // Clear the file input field when a text is selected 
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
      setFile(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if ((!text || text.trim().length === 0) && !file) {
      setMessage('Text or file input is missing');
      setTimeout(() => setMessage(''), 3000);
      return;
    }
    const formData = new FormData();
    if (text) {
      formData.append('text', text);
    }
    if (file) {
      formData.append('file', file);
    }

    try {
      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setMessage(response.data.message);
      setTimeout(() => setMessage(''), 3000);
    } catch (error) {
      if (error.response) {
        // The request was made and the server responded with a status code that does not fall in the range of 2xx 
        console.error('Error uploading file, data:', error.response.data);
        console.error('Error status:', error.response.status);
        console.error('Error headers:', error.response.headers);
        setMessage(error.response.data.error || 'File upload failed.');
      } else if (error.request) {
        // The request was made but no response was received 
        console.error('Error request:', error.request);
        setMessage('No response received from server.');
      } else {
        // Something happened in setting up the request that triggered an Error 
        console.error('Error message:', error.message);
        console.error('Error config:', error.config);
        setMessage('Request setup failed.');
      }
      setTimeout(() => setMessage(''), 3000);
    }
  };


  return (
    <div>
      <h1>Upload Form</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Text:</label>
          <input type="text" value={text} onChange={handleTextChange} ref={textInputRef} />
        </div>
        <div>
          <label>File:</label>
          <input type="file" onChange={handleFileChange} ref={fileInputRef} />
          {file && (
            <div> 
              <button type="button" onClick={handleFileRemove}>Unselect File</button> 
              </div>
            )}
        </div>
        <button type="submit">Submit</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
