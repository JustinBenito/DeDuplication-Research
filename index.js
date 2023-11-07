import weaviate from 'weaviate-ts-client';
import fs from 'fs';

const client = weaviate.client({
    scheme: 'http',
    host: 'localhost:8080',
});

const schemaRes = await client.schema.getter().do();

console.log(schemaRes)

const img = fs.readFileSync('./img/lung1.jpeg', 'utf-8');

const b64 = Buffer.from(img).toString('base64');

await client.data.creator()
  .withClassName('Meme')
  .withProperties({
    image: b64,
    text: 'lungs'
  })
  .do();