import { useState } from 'react';
import axios from 'axios';

export default function Upload() {
  const [text, setText] = useState('');
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('text', text);
    formData.append('file', file);
  
    try {
      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('File uploaded successfully', response.data);
    } catch (error) {
      console.error('Error uploading file', error.response.data);
    }
  };
  

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Text:</label>
        <input 
          type="text" 
          value={text} 
          onChange={(e) => setText(e.target.value)} 
        />
      </div>
      <div>
        <label>File:</label>
        <input 
          type="file" 
          onChange={handleFileChange} 
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}
