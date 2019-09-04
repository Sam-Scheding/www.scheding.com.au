import Vue from 'vue';
import { storiesOf } from '@storybook/vue';
import Grid from './Index.vue';

storiesOf('Grid', module)
.add('with text', () => ({
   render: h => h(Grid, {
     props: {
       backgroundColour: '#FFFFFF',
     }
   })
}))
