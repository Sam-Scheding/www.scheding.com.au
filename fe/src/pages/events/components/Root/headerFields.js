const formatDate = value => {
  if (value) {
    const dt = new Date(value);
    return `${addZero(dt.getDate())}/${addZero(
      dt.getMonth() + 1
    )}/${dt.getFullYear()}`;
  }
  return "";
};
const addZero = value => ("0" + value).slice(-2);

export default [
  '__slot:checkboxes',
  {
    name: "firstName",
    label: "First Name",
    sortable: true
  },
  {
    name: "lastName",
    label: "Last Name",
    sortable: true
  },
  {
    name: "hometown",
    label: "Hometown",
    sortable: true,
    customElement: 'HometownNew'
  },
  {
    name: "dob",
    label: "Data of Birght",
    sortable: true
  },
  {
    name: "created",
    customHeader: "createdHeader",
    label: "Created",
    sortable: true,
    format: formatDate
  },
  {
    name: "updated",
    customHeader: true,
    sortable: true,
    format: formatDate
  },
  "__slot:actions:actionFirst",
  "__slot:actions"
];
