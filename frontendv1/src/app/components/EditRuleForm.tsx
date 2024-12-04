"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Rule } from "../../../types";

export default function EditRuleForm({ id, example, description }: Rule) {
    const [newExample, setNewExample] = useState(example);
    const [newDescription, setNewDescription] = useState(description);

    const router = useRouter();

    interface EditRuleFormProps {
        id: string;
        name: string;
        details: string;
    }

    interface RuleUpdateResponse {
        ok: boolean;
    }

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>): Promise<void> => {
        e.preventDefault();

        try {
            const res: RuleUpdateResponse = await fetch(`http://localhost:3000/api/rules/${id}`, {
                method: "PUT",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({ newExample, newDescription }),
            });

            if (!res.ok) {
                throw new Error("Failed to update rule");
            }

            router.refresh();
            router.push("/");
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
            <input
                onChange={(e) => setNewExample(e.target.value)}
                value={newExample}
                className="border border-slate-500 px-8 py-2"
                type="text"
                placeholder="Rule Example"
            />

            <input
                onChange={(e) => setNewDescription(e.target.value)}
                value={newDescription}
                className="border border-slate-500 px-8 py-2"
                type="text"
                placeholder="Rule Details"
            />

            <button className="bg-green-600 font-bold text-white py-3 px-6 w-fit">
                Update Rule
            </button>
        </form>
    );
}