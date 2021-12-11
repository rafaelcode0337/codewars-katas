function arrayDiff(arr1, arr2) {
  return arr1.filter(num => !arr2.includes(num));
}
