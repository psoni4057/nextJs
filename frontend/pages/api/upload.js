// pages/api/upload.js
// Backend API Routes: handle the incoming multipart request on the server side using Formidable in Next.js

import formidable from 'formidable';
import { promises as fs } from 'fs';

export const config = {
    api: {
        bodyParser: false,
    },
};

const handler = async (req, res) => {
    /*     if (req.method !== 'POST') {
            return res.status(405).send('Method Not Allowed');
        } */
    const form = formidable({ multiples: true, uploadDir: './uploads', keepExtensions: true });
    try {
        const { fields, files } = await new Promise((resolve, reject) => {
            form.parse(req, (err, fields, files) => {
                if (err) reject(err);
                else resolve({ fields, files });
            });
        });

        const text = fields.text;
        const file = files.file; // Assuming the file input name is "file"
        if (!text && !file) {
            return res.status(400).json({ error: "Text or file missing." });
        }
        if (file && file.size === 0) {
            return res.status(400).json({ error: "The file is empty." });
        }

        try {
            if (file) {
                const filePath = Array.isArray(file) ? file[0].filepath : file.filepath;
                const fileContent = await fs.readFile(filePath, 'utf8');
                res.status(200).json({ message: "Request fulfilled successfully.File is valid.", fileContent: fileContent.toString() });
            } else {
                res.status(200).json({ message: "Request fulfilled successfully.Text is valid.", text: text });
            }
        } catch (err) {
            console.error('Request processing error:', err);
            res.status(500).json({ error: "An error occurred while processing the request." });
        }
    } catch (err) {
        console.error('Unexpected error:', err); return res.status(500).json({ error: "An unexpected error occurred." });
    }
};

export default handler;
