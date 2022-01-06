import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/ |\n/);

const beg_number :number = Number(input[0])
const beg_threshold_number :number = Number(input[1])
const beg_price :number = Number(input[2])
const beg_added_price :number = Number(input[3])

// output();
const output = (x: any) => console.log(x)

if (beg_number > beg_threshold_number){
	output(beg_price * beg_threshold_number + (beg_number - beg_threshold_number) * beg_added_price)
} else {
	output(beg_price * beg_number)
}
	