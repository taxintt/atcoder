import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(' |\n');
const output = (x: any) => console.log(x)

// 暗黙の型変換で、文字列扱いで結合処理されないようにする
// see https://uxmilk.jp/11582
let base_num: number = Number(input[0]);
const threshold_num: number = Number(input[1]);

let counter = 0;

while (true) {
	if (threshold_num <= base_num) {
		break;
	}
	base_num += 10;
	counter += 1;
}

output(counter);
