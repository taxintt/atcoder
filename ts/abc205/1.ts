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

interface NumberDict {
	[name: number]: number;
  }
  

function main() {
	// write code
	const length = parseInt(lines[0])

	const numbers: NumberDict = {};
	const numArray: number[] = parseIntArray(lines[1])

	numArray.map((x: number) => (numbers[x] || 0) + 1);
	const isNotDuplicated = Object.keys(numbers).every((x: any) => {
		console.log(numbers[x]);
		numbers[x] == 1
	})

	const predictedSum = (length * (length+1)) / 2
	const sum = numArray.reduce(function(a: number, b: number){
		return a + b;
	});

	if (isNotDuplicated && (predictedSum==sum)){
		output("Yes")
	} else {
		output("No")
	}
}

// execute main function
main()