import { useState } from 'react';
import axios from 'axios';

//send the request from the client side

export default function Upload() {
  const [text, setText] = useState('');
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if ((!text || text.trim().length === 0) && !file) {
      //return res.status(400).json({ error: 'Text or file input is missing' });
      setMessage('Text or file input is missing');
    }
    const formData = new FormData();
    if (text) {
      formData.append('text', text);
    }
    if (file) {
      formData.append('file', file);
    }


    const isFormDataEmpty = () => {
      for (let key of formData.keys()) {
        return false; // If there's at least one key, the FormData is not empty
      }
      return true; // If no keys, the FormData is empty
    };

    if (isFormDataEmpty()) {
      console.log('FormData is empty.');
    } else {
      console.log('FormData contains data.');
    }


    try {
      //const response = await axios.post('/api/upload', formData, {
      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('File uploaded successfully', response.data);
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
        setMessage('Request setup failed.');
      }
      console.error('Error config:', error.config);
     // setMessage('Upload failed.');
    }
  };


  return (
    <div>
      <h1>Upload Form</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Text:</label>
          <input type="text" value={text} onChange={handleTextChange} />
        </div>
        <div>
          <label>File:</label>
          <input type="file" onChange={handleFileChange} />
        </div>
        <button type="submit">Submit</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
