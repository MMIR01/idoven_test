const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://www.debugbear.com/test/',
    supportFile: false,
    specPattern: "**/*.spec.js"
  },
})