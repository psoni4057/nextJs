"use client";

import { HiOutlineTrash } from "react-icons/hi";
import { useRouter } from "next/navigation";
import { Rule } from "../../../types";



export default function RemoveBtn({ id }: { id: Rule['id'] }) {
  const router = useRouter();
  const removeRule = async () => {
    const confirmed = confirm("Are you sure?");

    if (confirmed) {
      const res = await fetch(`http://localhost:3000/api/rules?id=${id}`, {
        method: "DELETE",
      });

      if (res.ok) {
        router.refresh();
      }
    }
  };

  return (
    <button onClick={removeRule} className="text-red-400">
      <HiOutlineTrash size={24} />
    </button>
  );
}