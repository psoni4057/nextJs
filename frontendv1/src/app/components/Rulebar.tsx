'use client'
import Link from "next/link";

export default function Rulebar() {
  return (
    <nav className="flex justify-between items-center bg-slate-800 px-8 py-3">
      <Link className="text-white font-bold" href={"/"}>
        Set Rule.
      </Link>
      <Link className="bg-white p-2" href={"/addRule"}>
        Add Rules
      </Link>
    </nav>
  );
}