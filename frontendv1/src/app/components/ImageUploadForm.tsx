import React, { useState } from 'react';

const ImageUploadForm = () => {
    const [selectedImage, setSelectedImage] = useState<File | null>(null);
    const [previewUrl, setPreviewUrl] = useState('');

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const files = event.target.files;
        if (files && files[0] && files[0].type.startsWith('image/')) {
            const file = files[0];
            setSelectedImage(file);
            setPreviewUrl(URL.createObjectURL(file)); // Create a preview URL for the selected image
        } else {
            alert('Please select a valid image file.');
        }
    };

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        if (selectedImage) {
            // You can add your validation logic here
            alert(`Validated image: ${selectedImage.name}`);
        } else {
            alert('Please upload an image file.');
        }
    };

    return (
        <form 
            onSubmit={handleSubmit} 
            className="max-w-sm mx-auto p-4 bg-white shadow-md rounded"
        >
            <div className="mb-4">
                <label 
                    htmlFor="imageUpload" 
                    className="block text-gray-700 text-sm font-bold mb-2"
                >
                    Upload Image
                </label>
                <input 
                    type="file" 
                    id="imageUpload" 
                    accept="image/*" 
                    onChange={handleFileChange} 
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                    required
                />
            </div>
            {previewUrl && (
                <div className="mb-4">
                    <img src={previewUrl} alt="Preview" className="rounded w-full h-auto mb-2" />
                </div>
            )}
            <button 
                type="submit" 
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
                Validate
            </button>
        </form>
    );
};

export default ImageUploadForm;