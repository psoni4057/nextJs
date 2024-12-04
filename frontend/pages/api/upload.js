// pages/api/upload.js
// Backend API Routes: handle the incoming multipart request on the server side using Formidable in Next.jsAPI routes

import formidable from 'formidable';
import fs from 'fs';

export const config = {
    api: {
        bodyParser: false,
    },
};

const handler = async (req, res) => {
    const form = formidable({ multiples: true, uploadDir: './uploads', keepExtensions: true });

    form.parse(req, (err, fields, files) => {
        if (err) {
            console.error('Form parse error:', err);
            return res.status(500).json({ error: err.message });
        }

        // Check text field
        const text = fields.text;
        console.log(text);
        const file = files.file; // Assuming the file input name is "file"
        if (!text && !file) {
            return res.status(400).json({ error: "Text or file missing." });
        }
        if (file && file.size === 0) {
            return res.status(400).json({ error: "The file is empty." });
        }

        try {
            // Process the file (dummy processing in this example) 
            if (file) {
                const filePath = Array.isArray(file) ? file[0].filepath : file.filepath;
                const fileContent = fs.readFileSync(filePath);
                res.status(200).json({ message: "File is valid.", fileContent: fileContent.toString() });
            } else{
                res.status(200).json({ message: "Text are valid.", text: text });
            }
            
        } catch (err) {
            console.error('File processing error:', err);
            res.status(500).json({ error: "An error occurred while processing the file." });
        }
    });
};

export default handler;
