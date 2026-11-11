import {cp,mkdir,copyFile,writeFile,readFile} from 'node:fs/promises';
import {resolve} from 'node:path';
const root=resolve(import.meta.dirname,'..');
await mkdir(resolve(root,'dist/vendor'),{recursive:true});
await cp(resolve(root,'src'),resolve(root,'dist'),{recursive:true});
await copyFile(resolve(root,'node_modules/phaser/dist/phaser.min.js'),resolve(root,'dist/vendor/phaser.min.js'));
await copyFile(resolve(root,'node_modules/phaser/LICENSE.md'),resolve(root,'dist/vendor/PHASER-LICENSE.md'));
let css=await readFile(resolve(root,'dist/style.css'),'utf8');
for(const name of ['ui','display']){const font=await readFile(resolve(root,'src/assets/fonts/'+name+'.ttf'));css=css.replace('./assets/fonts/'+name+'.ttf','data:font/ttf;base64,'+font.toString('base64'));}
await writeFile(resolve(root,'dist/style.css'),css);
await writeFile(resolve(root,'dist/.nojekyll'),'');
console.log('Built standalone static game → dist/ (no CDN, no server runtime)');
