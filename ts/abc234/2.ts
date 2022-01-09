import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/\n/);

const num : number = Number(input[0])

// output();
const output = (x: any) => console.log(x)

let result : number = 0

for (let base_index = 1; base_index < num+1; base_index++) {
	const base_pointx : number = input[base_index].split(/ /)[0];
	const base_pointy : number = input[base_index].split(/ /)[1];

	for (let index = 1; index < num+1; index++) {
		const pointx : number = input[index].split(/ /)[0];
		const pointy : number = input[index].split(/ /)[1];
		
		const calced_result : any = Math.sqrt((base_pointx - pointx)**2 + (base_pointy - pointy)**2)
		if (calced_result > result)  {
			result = calced_result
		}
	}
}

output(result)
