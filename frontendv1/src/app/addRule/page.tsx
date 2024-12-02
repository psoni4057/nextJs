"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AddTopic() {
  const [example, setExample] = useState("");
  const [description, setDescription] = useState("");

  const router = useRouter();

interface Topic {
    example: string;
    description: string;
}

const handleSubmit = async (e: React.FormEvent<HTMLFormElement>): Promise<void> => {
    e.preventDefault();

    if ( !description) {
        alert("Description is required.");
        return;
    }

    try {
        const res = await fetch("http://localhost:3000/api/topics", {
            method: "POST",
            headers: {
                "Content-type": "application/json",
            },
            body: JSON.stringify({ example, description } as Topic),
        });

        if (res.ok) {
            router.push("/");
        } else {
            throw new Error("Failed to create a rule");
        }
    } catch (error) {
        console.log(error);
    }
};

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-3">
      <input
        onChange={(e) => setExample(e.target.value)}
        value={example}
        className="border border-slate-500 px-8 py-2"
        type="text"
        placeholder="Example"
      />

      <input
        onChange={(e) => setDescription(e.target.value)}
        value={description}
        className="border border-slate-500 px-8 py-2"
        type="text"
        placeholder="Rule Description"
      />

      <button
        type="submit"
        className="bg-green-600 font-bold text-white py-3 px-6 w-fit"
      >
        Add Rule
      </button>
    </form>
  );
}