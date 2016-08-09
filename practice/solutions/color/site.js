'use strict';

/**
 * Return a byte as a two digit hex encoded string.
 */
function byteToHex(byte) {
  return _.pad(_.floor(byte).toString(16), 2, '0');
}

/**
 * Clamp a number to byte range, between 0 and 255.
 */
function clampByte(num) {
  return _.clamp(num, 0, 255);
}

/**
 * Create a new color from component R, G, and B values.
 *
 * Each value is a byte between 0 and 255.
 */
function Color(r, g, b) {
  this.rgb = [r, g, b];
}
Color.prototype = {
  /**
   * Additive blend two colors and return that new color.
   *
   * Components are added and then clamped to the range.
   */
  blendAdd: function(other) {
    var rgbPairs = _.zip(this.rgb, other.rgb);
    var addRGB = _.map(rgbPairs, _.sum);
    var clampedRGB = _.map(addRGB, clampByte);
    return new Color(clampedRGB[0], clampedRGB[1], clampedRGB[2]);
  },
  /**
   * Convert a color to it's CSS hex representaton as a string.
   */
  toHex: function() {
    return '#' + _.join(_.map(this.rgb, byteToHex), '');
  }
};

var yellow = new Color(255, 255, 0);
console.log(yellow.toHex());
var purple = new Color(255, 0, 255);
console.log(purple.toHex());
var white = yellow.blendAdd(purple);
console.log(white.toHex());
