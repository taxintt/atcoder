class PriorityQueue<T> {
	private list = new Array<T>();

	// 木の一番下(arrayだと右)に要素を追加する
	// 親の値は必ず子の値以上になる状態を満たすまで上に遡ってswapする
	// back = 実質left?
	public push(v: T) {
		this.list.push(v);
		const back = this.list.length - 1;
		this.compare(back);
	}

	private compare(child: number) {
		if (child === 0) return;
		// 木構造を踏まえた時に、[0,1]の場合にはparent=0となり[0,1,2,3,4]の場合はindexでchild=4(一番末尾のindex), parent=1となる
		const parent = Math.ceil(child / 2) - 1;

		const childValue = this.list[child];
		const parentValue = this.list[parent];

		// parentの値が大きくなる必要があるので、checkして必要に応じてswapする
		if (parentValue < childValue) {
			this.swap(child, parent);
			this.compare(parent);
		}
	}

	private swap(a: number, b: number) {
		const tmp = this.list[a];
		this.list[a] = this.list[b];
		this.list[b] = tmp;
	}

	public top(): T {
		if (this.list.length === 0) throw new Error("empty");
		return this.list[0];
	}

	public pop(): T {
		if (this.list.length === 0) throw new Error("empty");
		const ans = this.top();
		this.list[0] = this.list.pop();
		this.flow(0);
		return ans;
	}

	private flow(parent: number) {
		const parentValue = this.list[parent];

		const left = parent * 2 + 1;
		const right = parent * 2 + 2;

		if (!this.inRange(left)) return;

		// 左に子入るが右に子はいない
		if (this.inRange(left) && !this.inRange(right)) {
			const leftValue = this.list[left];

			if (parentValue < leftValue) {
				this.swap(parent, left);
			}
		}

		if (this.inRange(left) && this.inRange(right)) {
			const leftValue = this.list[left];
			const rightValue = this.list[right];
			const target = leftValue > rightValue ? left : right;
			const targetValue = this.list[target];

			if (parentValue < targetValue) {
				this.swap(parent, target);
				this.flow(target);
			}
		}
	}

	private inRange(index: number): boolean {
		return index < this.list.length;
	}

	public size() {
		return this.list.length;
	}

	public display() {
		console.log(this.list);
	}
}

function main() {
	const pq = new PriorityQueue<Number>();
	pq.push(8);
	pq.push(2);
	pq.push(10);
	pq.push(11);
	pq.display();
	console.log(pq.pop()); // 11
	pq.display();
	console.log(pq.pop()); // 10
}

main()