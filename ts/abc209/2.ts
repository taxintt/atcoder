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
	let [itemNumber, budget] = parseIntArray(lines[0])
	const itemPriceList = parseIntArray(lines[1])

	for (let index = 0; index < itemNumber; index++) {
		if (index % 2 == 1) {
			budget -= (itemPriceList[index]-1);
		} else {
			budget -= itemPriceList[index];
		}
		if (budget < 0) {
			return output('No')
		}
	}
	return output('Yes')
}

// execute main function
main()