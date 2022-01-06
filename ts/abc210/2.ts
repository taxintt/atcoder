import * as fs from 'fs';

const input: any = fs.readFileSync('/dev/stdin', 'utf8').split(/ |\n/);

const numbers_of_cards: number = Number(input[0]);
const characters: string = input[1];

// output();
const output = (x: any) => console.log(x)

// takahashi : odd / aoki: even
// see https://gist.github.com/aoi0308/6472388
for (let i: number = 0; i < numbers_of_cards; i++) {
	if (Number(characters[i]) == 1) {
		if (i % 2 == 0) {
			output("Takahashi")
			process.exit(0);
		} else {
			output("Aoki")
			process.exit(0);
		}
	}
  }


