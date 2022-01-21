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
   const [fennec, racoon]: number[] = parseIntArray(lines[0])
   const checkArray: number[] = [0,1,2]

   if (fennec === racoon) {
       output(checkArray.indexOf(fennec) && checkArray.indexOf(racoon))
   } else {
       output(Math.abs(3 - fennec - racoon))
   }
   
}

// execute main function
main()