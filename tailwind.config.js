/** @type {path.PlatformPath | path} */
const path = require('path');
const pySitePackages = path.join(__dirname, 'venv/Lib/site-packages');
let pyPackages = [];

if (pySitePackages) {
  pyPackages = [
      path.join(pySitePackages, 'crispy_tailwind/**/*.py'),
      path.join(pySitePackages, 'crispy_tailwind/**/*.js'),
      path.join(pySitePackages, 'crispy_tailwind/**/*.html')
  ];
}

module.exports = {
  content: ["templates/**/*.html", ...pyPackages],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/forms')
  ],
};

