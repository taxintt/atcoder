import * as fs from 'fs';


// input();
const lines: any = fs.readFileSync('/dev/stdin', 'utf8').split(/\n/);

function parseBigInt(line: string): BigInt {
	return BigInt(line)
}

function parseString(line: string): string {
	return line
}

function parseIntArray(line: string): number[] {
	return line.split(' ').map(v => parseInt(v));
}

function parseBigIntArray(line: string): BigInt[] {
	return line.split(' ').map(v => BigInt(v));
}

function parseStrArray(line: string): string[] {
	return line.split('');
}

// output();
const output = (x: any) => console.log(x)

const outputFromArray = (x: any[]) => x.map(x => console.log(x));

class PriorityQueue<T = number> {
	private data: T[] = Array(1)
	private tail = 1
	private compare: (a: T, b: T) => number

	constructor(compare: (a: T, b: T) => number) {
		this.compare = compare
	}

	get length() {
		return this.tail - 1
	}
	isEmpty() {
		return this.tail === 1
	}

	push(elem: T) {
		if (this.data.length <= this.tail) {
			this.data.push(elem)
		} else {
			this.data[this.tail] = elem
		}
		let i = this.tail
		let p = Math.floor(i / 2)
		this.tail++
		while (i > 1 && this.compare(this.data[p], elem) > 0) {
			this.data[i] = this.data[p]
			i = p
			p = Math.floor(i / 2)
		}
		this.data[i] = elem
	}

	top() {
		return this.tail === 1 ? undefined : this.data[1]
	}

	pop() {
		if (this.tail === 1) return undefined

		const top = this.data[1]
		this.data[1] = this.data[this.tail - 1]
		this.data[this.tail - 1] = undefined as any
		this.tail--
		this.maxHeapify(1)
		return top
	}

	private maxHeapify(i: number) {
		const left = Math.floor(i * 2)
		const right = left + 1

		let largest = i
		if (left < this.tail && this.compare(this.data[i], this.data[left]) > 0) {
			largest = left
		}
		if (right < this.tail && this.compare(this.data[largest], this.data[right]) > 0) {
			largest = right
		}

		if (largest !== i) {
			[this.data[i], this.data[largest]] = [this.data[largest], this.data[i]]
			this.maxHeapify(largest)
		}
	}
}

function main() {
	const [N, K] = parseIntArray(lines[0]);
	const P = parseIntArray(lines[1]);

	const pq = new PriorityQueue((a, b) => a - b);
	for (let i = 0; i < K; i++) pq.push(P[i]);

	const ans = [pq.top()];
	for (let i = K; i < N; i++) {
		if (P[i] > pq.top()) {
			pq.pop();
			pq.push(P[i]);
		}
		ans.push(pq.top());
	}

	// for (let i = 0; i < ans.length; i++) {
	// 	output(ans[i]);
	// }
	outputFromArray(ans)
}

main();
