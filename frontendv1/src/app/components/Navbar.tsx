'use client'
import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
const Navbar = () => {
  const path = usePathname();
 
  return (
   <nav className="bg-blue-600 text-white p-4">
    <div className="container mx-auto flex justify-between items-center">
      <img src="gdprlogo.png" alt="Logo" className="h-16 w-48 mr-2" />
      <a href="" className="text-2xl font-bold">
        GDPR Validator
      </a>
      <div>
        <Link href="Reports" className="mx-2 p-4 text-2xl">
        Reports
        </Link>
        <Link href="Rules" className="mx-2 p-4 text-2xl">
        Rules
        </Link>
        <Link href="Model" className="mx-2 p-4 text-2xl">
        Model
        </Link>
      </div>
    </div>
   </nav>
  );
};

export default Navbar;