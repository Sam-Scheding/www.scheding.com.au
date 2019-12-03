<template>
  <section class="events">
    <EventCard
      v-for="event in events"
      v-bind:key="event.id"
      v-bind:event="event"
    />
  </section>
</template>

<script>
import EventsService from '../../services/EventsService';
import EventCard from '../EventCard/Index.vue';

export default {
  name: 'Today',
  components: {
    EventCard,
  },
  data() {
    return {
      events: [],
    }
  },
  mounted() {
    this.setEvents();
  },
  methods: {
    async setEvents() {
      let today = new Date();
      let tomorrow = new Date();
      tomorrow.setDate(today.getDate()+1);
      this.events = await EventsService.getEvents(today, tomorrow);
    }
  }
}
</script>

<style scoped>
.events {
  display: flex;
  flex-wrap: wrap;
  padding-left: 50px;
  padding-right: 50px;
  justify-content: space-between;
}

</style>
