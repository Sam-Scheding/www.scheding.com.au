import Vue from 'vue';
import { storiesOf } from '@storybook/vue';
import Mystify from './Index.vue';
import { withKnobs, text, color, number } from '@storybook/addon-knobs';

const stories = storiesOf('Mystify', module);

stories.addDecorator(withKnobs);

stories.add('Default', () => ({
  components: { Mystify },
  template: `<Mystify></Mystify>`,
}))
.add('Custom', () => ({
  components: { Mystify },
  data: () => ({
    bg: color('Background Color', 'orange'),
    width: number('Width', 500),
    height: number('Height', 500),
    lines: number('Lines', 10),
    color: color('Line Color', '#000000'),
    thickness: number('Thickness', 3),
    speed: number('Speed', 2),
  }),
  template: `
    <Mystify
      v-bind:bg="bg"
      v-bind:color="color"
      v-bind:thickness="thickness"
      v-bind:speed="speed"
    />`,
}))
