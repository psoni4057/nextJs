'use client'
import React from "react";

import { usePathname } from "next/navigation";
import { Description, Field, Label, Textarea } from '@headlessui/react'
const Result = () => {
  const path = usePathname();
 
  return (
  
      <Field disabled className="mx-auto">
        <Label className="data-[disabled]:opacity-50 text-2xl">Result</Label>
        <Description className="data-[disabled]:opacity-50 text-2xl">Analysis of the result.</Description>
        <Textarea name="result" className="data-[disabled]:bg-gray-100"></Textarea>
      </Field>
   
  );
};

export default Result;