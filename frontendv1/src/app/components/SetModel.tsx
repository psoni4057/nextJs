'use client'
import React, { useState } from 'react';
import {setModelKey,setModelName} from "@/redux/features/model-slice";
import {useDispatch} from "react-redux";
import type { AppDispatch } from "@/redux/store";

const SetModel = () => {
  const [selectedOption, setSelectedOption] = useState('OpenAI');
  const [key, setKey] = useState('');

   const dispatch = useDispatch<AppDispatch>();
interface OptionChangeEvent extends React.ChangeEvent<HTMLSelectElement> {}

const handleOptionChange = (event: OptionChangeEvent) => {
    setSelectedOption(event.target.value);
};
const handleClick = () => {
    dispatch(setModelName(selectedOption));
    dispatch(setModelKey(key));
}

interface KeyChangeEvent extends React.ChangeEvent<HTMLTextAreaElement> {}

const handleKeyChange = (event: KeyChangeEvent) => {
    setKey(event.target.value);
};

  return (
    <div className="p-4">
      <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="options">
        Select Option
      </label>
      <select
        id="options"
        value={selectedOption}
        onChange={handleOptionChange}
        className="border border-gray-300 rounded-md p-2 mb-4"
      >
        <option value="OpenAI">OpenAI</option>
        <option value="Gemini">Gemini</option>
      </select>

      <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="key">
        Key
      </label>
      <textarea
        id="key"
        value={key}
        onChange={handleKeyChange}
        className="border border-gray-300 rounded-md p-2 mb-4 w-full h-24"
      />
    <button
        onClick={handleClick}
        className="bg-blue-500 text-white font-bold py-2 px-4 rounded"
    >
        Use Model
    </button>
    </div>
  );
};

export default SetModel;