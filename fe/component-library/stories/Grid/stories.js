import Vue from 'vue';
import { storiesOf } from '@storybook/vue';
import Grid from './Index.vue';
import { withKnobs, text, color, number } from '@storybook/addon-knobs';

const stories = storiesOf('Grid', module);

stories.addDecorator(withKnobs);

stories.add('Default', () => ({
  components: { Grid },
  template: `<Grid></Grid>`,
}))
.add('Custom', () => ({
  components: { Grid },
  data: () => ({
    bg: color('Background Color', '#FFFFFF'),
    color: color('Line Color', '#000000'),
    horizon: number('Horizon', 0),
    thickness: number('Thickness', 3),
    speed: number('Speed', 2),
  }),
  template: `
    <Grid
      v-bind:bg="bg"
      v-bind:color="color"
      v-bind:horizon="horizon"
      v-bind:thickness="thickness"
      v-bind:speed="speed"
    />`,
}))
