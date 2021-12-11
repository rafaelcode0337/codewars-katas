export function arrayDiff(arr1: number[], arr2: number[]): number[] {
  return arr1.filter(num => !arr2.includes(num));
}
