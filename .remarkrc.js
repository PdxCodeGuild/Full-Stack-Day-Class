"use strict";

module.exports = {
  "plugins": {
    "remark-lint": {
      "final-newline": true,
      "list-item-indent": "mixed",
      "maximum-line-length": false,
      "ordered-list-marker-value": "single",
      "strong-marker": "*",
      "unordered-list-marker-style": "*",
      "fenced-code-flag": {
        "allowEmpty": true
      },
      "no-emphasis-as-heading": false
    },
    "remark-validate-links": {}
  }
};
