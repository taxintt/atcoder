import * as fs from 'fs';


// input();
const lines: any = fs.readFileSync('/dev/stdin', 'utf8').split(/\n/);

function parseBigInt(line: string): BigInt {
   return BigInt(line)
}

function parseString(line: string): string {
   return line
}

function parseIntArray(line: string): number[] {
   return line.split(' ').map(v => parseInt(v));
}

function parseBigIntArray(line: string): BigInt[] {
   return line.split(' ').map(v => BigInt(v));
}
   
function parseStrArray(line: string): string[] {
   return line.split('');
}

// output();
const output = (x: any) => console.log(x)

const outputFromArray = (x: any[]) => x.map(x => console.log(x));


function main() {
   // write code
   const word: string = lines[0]
   const [position_a, position_b] :number[] = parseIntArray(lines[1])

   const a: string = word.slice(position_a-1, position_a)
   const b: string = word.slice(position_b-1, position_b)

   if (position_a!=1 && position_b!=(word.length-1)) {
       output(word.slice(0, position_a) + b + word.slice(position_a, position_b) + a + word.slice(position_a));
   } else if (position_a==1 && position_b!=(word.length-1)) {
       output(b + word.slice(position_a, position_b) + a + word.slice(position_a));
   } else if (position_a!=1 && position_b==(word.length-1)) {
       output(word.slice(0, position_a) + b + word.slice(position_a, position_b) + a);
   } else {
       output(b + word.slice(position_a, position_b) + a);
   }
}   

// execute main function
main()