import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/ |\n/);

// output();
const output = (x: any) => console.log(x)

const avg_blood_presure: number = Number(input[0]);
const converged_blood_presure: number = Number(input[1]);

output(((avg_blood_presure - converged_blood_presure) / 3) + converged_blood_presure)