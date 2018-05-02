let regex = /\d+([,.]\d+)?/

export function cssMultiply(string, multiplier) {
  return string.replace(regex, num => parseFloat(num) * multiplier)
}
