'use client'
import Navbar from "./components/Navbar";
import Tabs from "./components/Tabs";
import Result from "./components/Result";

import { useAppSelector } from "@/redux/store";

export default function Home() {
  
  const modelName = useAppSelector((state) => state.modelReducer.value.modelName);
  const modelKey = useAppSelector((state) => state.modelReducer.value.modelKey);

  return (
    <div >
      <Navbar />
      <Tabs />
    
      <Result />
      <div>
      <p>Model Name: {modelName}</p>
      <p>Model Key: {modelKey}</p>
      </div>
    </div>
  );
}