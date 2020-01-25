<template>
  <div class="">
    <p>Hello World</p>
    <EventsDataTable
      v-bind:header-fields="headerFields"
      v-bind:data="data"
    />
  </div>
</template>

<script>
import EventsDataTable from '../../../../components/EventsDataTable/Index.vue';
import initialData from './initialData';
import headerFields from './headerFields';

export default {
  name: 'Root',
  components: {
    EventsDataTable,
  },
  data: () => {
    return {
      headerFields,
      data: initialData.slice(0, 10),
    }
  }
}
</script>

<style scoped>

</style>
