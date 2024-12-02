'use client'
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'
import TextInputForm from './TextInputForm';
import PdfUploadForm from './PdfUploadForm';
import ImageUploadForm from './ImageUploadForm';

const Tabs = () => {
  return (
    <div className="w-full max-w-md px-2 py-16 sm:px-0 mx-auto" >
    <TabGroup>
      <TabList className="flex space-x-1 rounded-xl bg-blue-900/20 p-1">
        <Tab className="w-full rounded-lg py-2.5 text-2xl font-medium leading-5 text-blue-700">Text</Tab>
        <Tab className="w-full rounded-lg py-2.5 text-2xl font-medium leading-5 text-blue-700">PDF</Tab>
        <Tab className="w-full rounded-lg py-2.5 text-2xl font-medium leading-5 text-blue-700">Image</Tab>
      </TabList>
      <TabPanels className="mt-2">
        <TabPanel className="rounded-xl bg-white p-3"><TextInputForm /></TabPanel>
        <TabPanel className="rounded-xl bg-white p-3"><PdfUploadForm /></TabPanel>
        <TabPanel className="rounded-xl bg-white p-3"><ImageUploadForm /></TabPanel>
      </TabPanels>
    </TabGroup>
    </div>
  )
};
export default Tabs;