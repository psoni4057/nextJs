import formidable from 'formidable';
import fs from 'fs';

export const config = {
  api: {
    bodyParser: false,
  },
};

export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).send('Method Not Allowed');
  }

  const form = formidable({ multiples: true, uploadDir: './uploads', keepExtensions: true });

  form.parse(req, (err, fields, files) => {
    if (err) {
      console.error('Error parsing form:', err);
      return res.status(500).json({ error: 'Error parsing the form data' });
    }

    const text = fields.text;
    const file = files.file;

    if (!text || !file) {
      return res.status(400).json({ error: 'Text or file input is missing' });
    }

    const oldPath = Array.isArray(file) ? file[0].filepath : file.filepath;
    const newPath = `./uploads/${Array.isArray(file) ? file[0].originalFilename : file.originalFilename}`;

    fs.rename(oldPath, newPath, (err) => {
      if (err) {
        console.error('Error moving file:', err);
        return res.status(500).json({ error: 'Error moving the file' });
      }
      res.status(200).json({ message: 'File uploaded successfully' });
    });
  });
}
