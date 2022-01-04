import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/\n/);
const output = (x: any) => console.log(x)

const start_character: number = Number(input[0]);
const last_character: number = Number(input[1]);
const characters: string = input[2];

// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/String/split#reversing_a_string_using_split
output(characters.slice(0, start_character - 1) + characters.slice(start_character - 1, last_character).split('').reverse().join('') + characters.slice(last_character, characters.length))

