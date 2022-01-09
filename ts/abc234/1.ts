import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/ |\n/);

const num: number = Number(input[0])

function return_value(n: number) {
	return (n ** 2) + (2 * n) + 3
}

// output();
const output = (x: any) => console.log(x)

output(return_value(return_value(return_value(num) + num) + return_value(return_value(num))))
