import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/\n/);

// output();
const output = (x: any) => console.log(x)

const max_num: number = input[0].split(" ")[0]
const k: number = input[0].split(" ")[1]

const value_array: [number] = input[1].split(' ').map((x: string) => Number(x));

for (let index = k; index <= max_num; index++) {
	let temp_array: number[] = value_array.slice(0, index).reverse()
	output(temp_array[k-1])
}

