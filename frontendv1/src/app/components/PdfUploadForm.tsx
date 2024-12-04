import React, { useState } from 'react';

const PdfUploadForm = () => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            setFile(event.target.files[0]);
        }
    };

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        if (file) {
            // You can add your validation logic here
            alert(`Validated file: ${file.name}`);
        } else {
            alert('Please upload a PDF file.');
        }
    };

    return (
        <form 
            onSubmit={handleSubmit} 
            className="max-w-sm mx-auto p-4 bg-white shadow-md rounded"
        >
            <div className="mb-4">
                <label 
                    htmlFor="pdfUpload" 
                    className="block text-gray-700 text-sm font-bold mb-2"
                >
                    Upload PDF
                </label>
                <input 
                    type="file" 
                    id="pdfUpload" 
                    accept="application/pdf" 
                    onChange={handleFileChange} 
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                    required
                />
            </div>
            <button 
                type="submit" 
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
                Validate
            </button>
        </form>
    );
};

export default PdfUploadForm;