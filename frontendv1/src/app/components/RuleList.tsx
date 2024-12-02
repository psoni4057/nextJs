import Link from "next/link";
import RemoveBtn from "./RemoveBtn";
import { HiPencilAlt } from "react-icons/hi";
import { Rule } from "../../../types";

const getRules = async () => {
  try {
    //const res = await fetch("http://localhost:3000/api/rules", {
    //  cache: "no-store",
    //});
    const res = {
      ok: true,
      json: async () => ({
        rules: [
          { id: 1, description: "Rule 1", example: "Example 1" },
          { id: 2, description: "Rule 2", example: "Example 2" },
          { id: 3, description: "Rule 3", example: "Example 3" },
        ],
      }),
    };

    if (!res.ok) {
      throw new Error("Failed to fetch rules");
    }

    return res.json();
  } catch (error) {
    console.log("Error loading rules: ", error);
  }
};

export default async function RulesList() {
  const data = await getRules();
  const rules = data?.rules || [];

  return (
    <>
      {rules.map((t: Rule) => (
        <div
          key={t.id}
          className="p-4 border border-slate-300 my-3 flex justify-between gap-5 items-start"
        >
          <div>
            <h2 className="font-bold text-2xl">{t.description}</h2>
            <div>{t.example}</div>
          </div>

          <div className="flex gap-2">
            <RemoveBtn id={t.id} />
            <Link href={`/editRule/${t.id}`}>
              <HiPencilAlt size={24} />
            </Link>
          </div>
        </div>
      ))}
    </>
  );
}