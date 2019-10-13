<template>
  <div class="a">
    <ul>
      <li v-for="event in events">
        {{ event.title }} | {{ event.start }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import parser from 'cron-parser';

export default {
  name: 'app',
  data () {
    return {
      rawEvents: [],
    }
  },
  computed: {
    events() {
      let events = []
      this.rawEvents.forEach(event => {
        let interval = parser.parseExpression(event.start);
        for (var i = 0; i < 100; i++) {
          console.log(event.start);
          events.push({
            title: event.title,
            start: interval.next().toString(),
          });
        }
        // console.log(event.title);
      });
      return events;
    }
  },
  mounted () {
    axios
      .get('http://localhost:8000/events/json')
      .then(response => {
        this.rawEvents = response.data;
      })
  }
}
</script>

<style>

</style>
