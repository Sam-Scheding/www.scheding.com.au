import { configure } from '@storybook/vue';

const req = require.context('.', true, /stories\.js$/);

function loadStories() {
  req.keys().forEach(filename => req(filename));
}

configure(loadStories, module);
