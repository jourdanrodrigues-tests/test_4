let regex = /\d+([,.]\d+)?/

export function cssMultiply(string, multiplier) {
  return string.replace(regex, num => parseFloat(num) * multiplier)
}

export const mediaMobile = '@media (max-width: 768px)'

export const mediaDesktop = '@media (min-width: 769px)'
