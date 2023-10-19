let n: number = Date.now();

export default function (): string {
    return (++n).toString(36);
}
