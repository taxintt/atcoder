import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/ |\n/).filter((n:any) => n);

// output();
const output = (x: any) => console.log(x)

var hashMap: { [key: string]: number; } = { "H": 0, "2B": 0, "3B": 0, "HR": 0 };

// H , 2B , 3B , HR
input.map((i: string) => {
	hashMap[i] += 1; 
});

if (hashMap["H"] == 1 && hashMap["2B"] == 1 && hashMap["3B"] == 1 && hashMap["HR"] == 1) {
	output("Yes")
} else {
	output("No")
}

