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
	const n: number = parseInt(lines[0])
	let counter: number = 0

	while (true) {
		counter += 1
		if ((counter * (counter+1)/2) >= n) {
			break
		}
	}
	output(counter)
}

// execute main function
main()