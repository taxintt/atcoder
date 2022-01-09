import * as fs from 'fs';
import { Big } from 'big.js';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/ |\n/);

// output();
const output = (x: any) => console.log(x)

// 10 進法で表記したときに 0,2 のみからなる正整数のうち、 K 番目に小さいものを求めてください。
// 小さい方から並べると、 2,20,22,200,202,220,222,2000 となります。

// number型では桁落ちが発生する... → bigintを使いましょう
// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/BigInt
// console.log({max: Number.MAX_SAFE_INTEGER, min: Number.MIN_SAFE_INTEGER});
// {max: 9007199254740991, min: -9007199254740991}

const num: any = BigInt(input[0])
const characters: string = num.toString(2).replace(/1/g, '2')

output(characters)