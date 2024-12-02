'use client'
import React, { useState } from 'react';

const TextInputForm = () => {
    const [inputText, setInputText] = useState('');

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInputText(e.target.value);
    };

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        // You can add your validation logic here
        alert(`Validated text: ${inputText}`);
    };

    return (
        <form 
            onSubmit={handleSubmit} 
            className="max-w-sm mx-auto p-4 bg-white shadow-md rounded"
        >
            <div className="mb-4">
                <label 
                    htmlFor="inputText" 
                    className="block text-gray-700 text-sm font-bold mb-2"
                >
                    Enter the text
                </label>
                <input 
                    type="text" 
                    id="inputText" 
                    value={inputText} 
                    onChange={handleInputChange} 
                    placeholder="Type something..." 
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

export default TextInputForm;