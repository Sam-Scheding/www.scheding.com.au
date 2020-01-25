
<script>
import { DataTable } from 'v-datatable-light';
import orderBy from 'lodash.orderby'

export default {
  name: "EventsDataTable",
  components: {
    DataTable
  },
  props: {
    data: {
      type: Array,
      required: true,
    },
    headerFields: {
      type: Array,
      required: true,
    },
  },
  data: () => {
    return {
      isLoading: false,
      sort: "asc",
      sortField: "firstName",
      listItemsPerPage: [5, 10, 20, 50, 100],
      itemsPerPage: 10,
      currentPage: 1,
      totalItems: 16,
      hometown: null,
      datatableCss: {
        table: 'table table-bordered table-hover table-striped table-center',
        th: 'header-item',
        thWrapper: 'th-wrapper',
        thWrapperCheckboxes: 'th-wrapper checkboxes',
        arrowsWrapper: 'arrows-wrapper',
        arrowUp: 'arrow up',
        arrowDown: 'arrow down',
        footer: 'footer'
      },
    }
  },
  methods: {
    dtEditClick: props => alert("Click props:" + JSON.stringify(props)),
    dtUpdateSort: function ({ sortField, sort }) {
      const sortedData = orderBy(this.initialData, [sortField],[sort]);
      const start = (this.currentPage -1) * this.itemsPerPage;
      const end = this.currentPage * this.itemsPerPage;
      this.data = sortedData.slice(start, end)
    },
    updateItemsPerPage: function (itemsPerPage) {
      this.itemsPerPage = itemsPerPage
      if (itemsPerPage >= this.initialData.length) {
        this.data = this.initialData
      } else {
        this.data = this.initialData.slice(0, itemsPerPage)
      }
    },
    changePage: function (currentPage) {
      this.currentPage = currentPage
      const start = (currentPage -1) * this.itemsPerPage;
      const end = currentPage * this.itemsPerPage;
      this.data = this.props.initialData.slice(start, end)
    },
    updateCurrentPage: function (currentPage) {
      this.currentPage = currentPage
    },
    changeHometown: function (event, id) {
      this.data = this.data.map(item => (item.id === id ? { ...item, hometown: event.target.value } : item))
    },
    actionFirstClick: (params) => {
      alert(JSON.stringify(params))
    }
  }
}

</script>

<template lang="html">
  <DataTable
    v-bind:header-fields="headerFields"
    v-bind:data="data"
    v-bind:css="datatableCss"
  />
</template>

<style lang="css" scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#app .title {
  margin-bottom: 30px;
}
#app .items-per-page {
  height: 100%;
  display: flex;
  align-items: center;
  color: #337ab7;
}
#app .items-per-page label {
  margin: 0 15px;
}
/* Datatable CSS */
.v-datatable-light .header-item {
  cursor: pointer;
  color: #337ab7;
  transition: color 0.15s ease-in-out;
}
.v-datatable-light .header-item:hover {
  color: #ed9b19;
}
.v-datatable-light .header-item.no-sortable{
  cursor: default;
}
.v-datatable-light .header-item.no-sortable:hover {
  color: #337ab7;
}
.v-datatable-light .header-item .th-wrapper {
  display: flex;
  width: 100%;
  height: 100%;
  font-weight: bold;
}
.v-datatable-light .header-item .th-wrapper.checkboxes {
  justify-content: center;
}
.v-datatable-light .header-item .th-wrapper .arrows-wrapper {
  display: flex;
  flex-direction: column;
  margin-left: 10px;
  justify-content: space-between;
}
.v-datatable-light .header-item .th-wrapper .arrows-wrapper.centralized {
  justify-content: center;
}
.v-datatable-light .arrow {
  transition: color 0.15s ease-in-out;
  width: 0;
  height: 0;
  border-left: 8px solid transparent;
  border-right: 8px solid transparent;
}
.v-datatable-light .arrow.up {
  border-bottom: 8px solid #337ab7;
}
.v-datatable-light .arrow.up:hover {
  border-bottom: 8px solid #ed9b19;
}
.v-datatable-light .arrow.down {
  border-top: 8px solid #337ab7;
}
.v-datatable-light .arrow.down:hover {
  border-top: 8px solid #ed9b19;
}
.v-datatable-light .footer {
  display: flex;
  justify-content: space-between;
  width: 500px;
}
/* End Datatable CSS */
/* Pagination CSS */
 .v-datatable-light-pagination {
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin: 0;
    padding: 0;
    width: 300px;
    height: 30px;
  }
  .v-datatable-light-pagination .pagination-item {
    width: 30px;
    margin-right: 5px;
    font-size: 16px;
    transition: color 0.15s ease-in-out;
  }
  .v-datatable-light-pagination .pagination-item.selected {
    color: #ed9b19;
  }
  .v-datatable-light-pagination .pagination-item .page-btn {
    background-color: transparent;
    outline: none;
    border: none;
    color: #337ab7;
    transition: color 0.15s ease-in-out;
  }
  .v-datatable-light-pagination .pagination-item .page-btn:hover {
    color: #ed9b19;
  }
  .v-datatable-light-pagination .pagination-item .page-btn:disabled{
    cursor: not-allowed;
    box-shadow: none;
    opacity: .65;
  }
  /* END PAGINATION CSS */

  /* ITEMS PER PAGE DROPDOWN CSS */
  .item-per-page-dropdown {
    background-color: transparent;
    min-height: 30px;
    border: 1px solid #337ab7;
    border-radius: 5px;
    color: #337ab7;
  }
  .item-per-page-dropdown:hover {
    cursor: pointer;
  }
  /* END ITEMS PER PAGE DROPDOWN CSS */
</style>
